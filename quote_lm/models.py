from django.db import models
from django.urls import reverse


class QuoteLm(models.Model):
    quote_id = models.CharField(max_length=30)
    # customer_id = models.CharField(max_length=20)
    # date = models.DateField()
    # length = models.PositiveIntegerField()
    # width = models.PositiveIntegerField()
    # height = models.PositiveIntegerField()
    # material = models.CharField(max_length=10)
    # surface_finish = models.CharField(max_length=10)
    # h_headers = models.PositiveIntegerField()
    # v_headers = models.PositiveIntegerField()
    # bubs_num = models.PositiveIntegerField()
    # drill_bar_num = models.PositiveIntegerField()
    # image = models.ImageField()


