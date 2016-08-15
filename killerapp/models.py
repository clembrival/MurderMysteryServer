from django.db import models
from django.utils import timezone

import re


class Entry(models.Model):
    title = models.CharField(max_length=100, default='?')
    year = models.CharField(max_length=4, default='?')
    detective = models.CharField(max_length=24, default='?')
    location = models.CharField(max_length=13, default='?')
    point_of_view = models.CharField(max_length=5, default='?')
    murder_weapon = models.CharField(max_length=10, default='?')
    victim_gender = models.CharField(max_length=4, default='?')
    murderer_gender = models.CharField(max_length=5, default='?')
    average_ratings = models.CharField(max_length=4, default='?')
    timestamp = models.DateTimeField(default=timezone.now, blank=False)

    def __unicode__(self):
        data = ""

        data += '{},'.format(str(self.title))
        data += str(self.year + ",")

        pattern = re.compile("[ ]+")
        if pattern.search(self.detective):
            data += '{},'.format(str(self.detective))
        else:
            data += str(self.detective + ",")

        data += str(self.location + ",")
        data += str(self.point_of_view + ",")
        data += str(self.murder_weapon + ",")
        data += str(self.victim_gender + ",")
        data += str(self.murderer_gender + ",")
        data += str(self.average_ratings)

        return data
