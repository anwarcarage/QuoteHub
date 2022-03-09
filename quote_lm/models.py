from django.db import models
from django.urls import reverse


class QuoteLm(models.Model):
    quote_id = models.CharField(max_length=30)
    customer_id = models.CharField(max_length=20)
    date = models.CharField(max_length=10)
    length = models.CharField(max_length=10)
    width = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    material = models.CharField(max_length=10)
    surface_finish = models.CharField(max_length=10)
    h_headers = models.CharField(max_length=10)
    v_headers = models.CharField(max_length=10)
    bubs_num = models.CharField(max_length=2)
    drill_bar_num = models.CharField(max_length=2)
    # image = models.CharField(max_length=30)


