import os

import json

from killerapp_server import settings
from killerapp.models import EntriesCount

from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt


# File storing the training set
filename = "dataset.arff"
filepath = os.path.join(settings.BASE_DIR, filename)


# Returns the number of entries in the dataset
def get_count(request):
    return HttpResponse(str(EntriesCount.objects.all()[0].count))


# Returns the content of the dataset file
def get_file(request):
    wrapper = FileWrapper(file(filename))
    return HttpResponse(wrapper, content_type='text/plain')


# Adds a given new entry to the dataset
@csrf_exempt
def update(request):

    if request.method != 'POST':
        return HttpResponse("ERROR")

    data = ""

    data_dict = json.loads(request.body)

    data += '"{}",'.format(str(data_dict['title']))
    data += str(data_dict['year'] + ",")
    data += '"{}",'.format(str(data_dict['detective']))
    data += str(data_dict['location'] + ",")
    data += str(data_dict['point_of_view'] + ",")
    data += str(data_dict['murder_weapon'] + ",")
    data += str(data_dict['victim_gender'] + ",")
    data += str(data_dict['murderer_gender'] + ",")
    data += str(data_dict['average_ratings'] + "\n")

    with open(filepath, "a") as dataset:
        dataset.write(data)
        entries_count = EntriesCount.objects.all()[0]
        entries_count.count += F('count') + 1
        entries_count.save()

    return HttpResponse("OK")
