from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    budget = models.FloatField(default=0)
    goal = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
