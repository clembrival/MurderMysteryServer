import os
import json

from killerapp_server import settings
from killerapp.models import Entry

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


# File storing the initial training set
filename = "dataset.arff"
# Path to the training set file
filepath = os.path.join(settings.BASE_DIR, filename)


# Returns the number of entries in the database and the id of the last entry
def get_count(request):
    return HttpResponse("%s\n%d" % (str(Entry.objects.all().count()),
                                    Entry.objects.order_by('-id')[0].id))


# Returns the timestamp of the newest database entry
def get_timestamp(request):
    return HttpResponse(str(Entry.objects.order_by('-timestamp')[0].timestamp))


# Returns the entries added after the last client update
@csrf_exempt
def get_new_entries(request):

    # Retrieve the timestamp of the client's last update
    client_last_update = request.GET['timestamp']

    # If the client has been updated before, return only the newest entries...
    if client_last_update:
        new_data = "".join([entry.__unicode__() for entry in \
                            Entry.objects.filter(timestamp__gte=client_last_update)])

    # ... otherwise return all the entries added after the initial training set entries
    else:
        new_data = "".join([entry.__unicode__() for entry in \
                            Entry.objects.filter(id__gt=66)])

    return HttpResponse(new_data)


# Adds a given new entry to the database, and returns the timestamp of the transaction
@csrf_exempt
def update(request):

    if request.method != 'POST':
        return HttpResponseBadRequest(None)

    data = []

    # Retrieve the data sent with the request
    data_dict = json.loads(request.body)

    data.append(str(data_dict['title']))
    data.append(data_dict['year'])
    data.append(str(data_dict['detective']))
    data.append(data_dict['location'])
    data.append(data_dict['point_of_view'])
    data.append(data_dict['murder_weapon'])
    data.append(data_dict['victim_gender'])
    data.append(data_dict['murderer_gender'])
    data.append(data_dict['average_ratings'])

    # Create new entry based on that data (or update existing entry)
    new_entry = add_entry(data)

    # Return the timestamp of the transaction
    return HttpResponse(str(new_entry.timestamp))


# Creates a new entry in the database, or updates an existing one, and returns the entry
def add_entry(data):
    entry = Entry.objects.get_or_create(title=data[0])[0]

    entry.year = data[1]
    entry.detective = data[2]
    entry.location = data[3]
    entry.point_of_view = data[4]
    entry.murder_weapon = data[5]
    entry.victim_gender = data[6]
    entry.murderer_gender = data[7]
    entry.average_ratings = data[8]

    entry.save()

    return entry
