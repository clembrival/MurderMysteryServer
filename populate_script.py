import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'killerapp_server.settings')

import django

django.setup()

from killerapp.models import EntriesCount


def populate():
    entries_count = EntriesCount.objects.get_or_create()[0]
    entries_count.save()

    print "Added initial entries count: %d" % entries_count.count


if __name__ == '__main__':
    print "Starting KillerApp population script..."
    populate()