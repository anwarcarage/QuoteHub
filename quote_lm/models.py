import datetime
from django.db import models


class QuoteLm(models.Model):
# customer variables
    NONE = ''
    BOEING_CANADA = 'BC'
    BOEING_SEATTLE = 'BS'
    BOEING_STLOUIS = 'BL'
    L3_HARRIS = 'L3'
    LOCKHEED = 'LM'
    NORTHROP = 'NG'
    SIKORSKY = 'SK'
    SPIRIT = "SP"

 # material type variables
    ALUMINUM = 'AL'
    STEEL = 'STL'
    INVAR = 'INV'

 # surface finish variables
    THIRTYTWORA = '32RA'
    SIXTYFOURRA = '64RA'
    ONETWENTYFIVERA = '125RA'

    CUSTOMER = [
        (NONE, 'Name...'),
        (BOEING_CANADA, 'Boeing Canada'),
        (BOEING_SEATTLE, 'Boeing Seattle'),
        (BOEING_STLOUIS, 'Boeing St.Louis'),
        (L3_HARRIS, 'L3 Harris'),
        (LOCKHEED, 'Lockheed Martin'),
        (NORTHROP, 'Northrop Grumman'),
        (SIKORSKY, 'Sikorsky'),
        (SPIRIT, 'Spirit'),
    ]

    MATERIAL = [
        (NONE, 'Type...'),
        (ALUMINUM, 'Aluminum'),
        (STEEL, 'Steel'),
        (INVAR, 'Invar'),
    ]

    SURFACEFINISH = [
        (NONE, 'Type...'),
        (THIRTYTWORA, '32 Ra'),
        (SIXTYFOURRA, '64 Ra'),
        (ONETWENTYFIVERA, '125 Ra'),
    ]

    quote_id = models.CharField(
        max_length=30,
        default=NONE
    )
    customer_id = models.CharField(
        max_length=30,
        choices=CUSTOMER,
        default=NONE
    )
    date = models.DateField(default=datetime.date.today())
    length = models.PositiveIntegerField(
        default=NONE
    )
    width = models.PositiveIntegerField(
        default=NONE
    )
    height = models.PositiveIntegerField(
        default=NONE
    )
    material = models.CharField(
        max_length=10,
        choices=MATERIAL,
        default=NONE
    )
    surface_finish = models.CharField(
        max_length=10,
        choices=SURFACEFINISH,
        default=NONE
    )
    h_headers = models.PositiveIntegerField(
        default=NONE
    )
    v_headers = models.PositiveIntegerField(
        default=NONE
    )
    bubs_num = models.PositiveIntegerField(
        default=NONE
    )
    drill_bar_num = models.PositiveIntegerField(
        default=NONE
    )
    # surface_area = models.PositiveIntegerField()
    # image = models.ImageField()



