import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'killerapp_server.settings')

import django

django.setup()

from killerapp_server import settings
from killerapp.models import Entry


def populate():

    filename = "dataset.arff"
    filepath = os.path.join(settings.BASE_DIR, filename)

    with open(filepath, "r") as dataset:
        for line in dataset:
            if line[0] == "'" or line[0].isalpha():
                print(add_entry(line.split(",")).__unicode__())



def add_entry(data):
    entry = Entry.objects.get_or_create(title=data[0])[0]

    entry.year = str(data[1])
    entry.detective = data[2]
    entry.location = str(data[3])
    entry.point_of_view = str(data[4])
    entry.murder_weapon = str(data[5])
    entry.victim_gender = str(data[6])
    entry.murderer_gender = str(data[7])
    entry.average_ratings = str(data[8]).strip("\n")

    entry.save()

    return entry


if __name__ == '__main__':
    print("Starting KillerApp population script...")
    populate()
