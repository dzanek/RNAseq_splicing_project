from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Query(models.Model):
    ''' Class to story queries for Array Express api '''
    query_id = models.CharField(max_length=6)
    keywords = models.CharField(max_length=2000)
    organism = models.CharField(max_length=200)
    experiment_type = models.CharField(max_length=200)

    def _to_list(self):
        ''' '''
        return [self.query_id, self.keywords, self.organism, self.experiment_type]

class Sample(models.Model):
    ''' Class to stori info about single array express record '''
    experiment_id = models.CharField(max_length=50)
    experiment_type = models.CharField(max_length=200)
    experiment_description = models.TextField()
    experiment_link = models.CharField(max_length=200)
