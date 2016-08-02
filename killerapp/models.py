from django.db import models


class EntriesCount(models.Model):

    count = models.IntegerField(default=66)
    