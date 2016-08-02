import os

from killerapp_server import settings
from killerapp.models import EntriesCount

from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.db.models import F


filename = "dataset.arff"
filepath = os.path.join(settings.BASE_DIR, filename)


def get_count(request):
    return HttpResponse(str(EntriesCount.objects.all()[0].count))


def get_file(request):
    wrapper = FileWrapper(file(filename))
    return HttpResponse(wrapper, content_type='text/plain')


def update(request):

    if request.method != 'POST':
        return HttpResponse("ERROR")

    data = ""

    data += str(request.POST.get('title') + ",")
    data += str(request.POST.get('year') + ",")
    data += str(request.POST.get('detective') + ",")
    data += str(request.POST.get('location') + ",")
    data += str(request.POST.get('point_of_view') + ",")
    data += str(request.POST.get('murder_weapon') + ",")
    data += str(request.POST.get('victim_gender') + ",")
    data += str(request.POST.get('murderer_gender') + ",")
    data += str(request.POST.get('average_ratings') + "\n")

    with open(filepath, "a") as dataset:
        dataset.write(data)
        entries_count = EntriesCount.objects.all()[0]
        entries_count.count += F('count') + 1
        entries_count.save()

    return HttpResponse("OK")
