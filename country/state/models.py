from django.db import models


class State(models.Model):
    state = models.CharField(null=True, blank=True, max_length=100)
    desc = models.CharField(null=True, blank=True, max_length=100)
    code = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.state


class City(models.Model):
    state = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(null=True, blank=True, max_length=100)
    desc = models.CharField(null=True, blank=True, max_length=100)
    code = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.city
