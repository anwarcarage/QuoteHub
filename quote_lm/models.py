import datetime
from django.db import models


class QuoteLm(models.Model):
# customer variables
    NONE = ''
    BOEING_CANADA = 'Boeing Canada'
    BOEING_SEATTLE = 'Boeing Seattle'
    BOEING_STLOUIS = 'Boeing St.Louis'
    L3_HARRIS = 'L3 Harris'
    LOCKHEED = 'Lockheed Martin'
    NORTHROP = 'Northrop Grumman'
    SIKORSKY = 'Sikorsky'
    SPIRIT = 'Spirit'

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
        default=NONE,
        unique=True
    )
    customer_id = models.CharField(
        max_length=30,
        choices=CUSTOMER,
        default=NONE
    )
    date = models.DateField(default=datetime.date.today())
    length = models.PositiveIntegerField(default=NONE)
    width = models.PositiveIntegerField(default=NONE)
    height = models.PositiveIntegerField(default=NONE)
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
    h_headers = models.PositiveIntegerField(default=NONE)
    v_headers = models.PositiveIntegerField(default=NONE)
    bubs_num = models.PositiveIntegerField(default=NONE)
    drill_bar_num = models.PositiveIntegerField(default=NONE)

    def __str__(self):
        return self.id


class CalcHour(models.Model):
    weld_hours = models.PositiveIntegerField(default='')
    fit_hours = models.PositiveIntegerField(default='')
    program_hours = models.PositiveIntegerField(default='')
    machine_hours = models.PositiveIntegerField(default='')
    bench_hours = models.PositiveIntegerField(default='')
    assembly_hours = models.PositiveIntegerField(default='')
    shipping_hours = models.PositiveIntegerField(default='')
    laser_hours = models.PositiveIntegerField(default='')
    inspect_hours = models.PositiveIntegerField(default='')
    total_hours = models.PositiveIntegerField(default='')
    quote_id = models.ForeignKey(QuoteLm, default=1, on_delete=models.SET_DEFAULT)


class CalcPrice(models.Model):
    weld_price = models.PositiveIntegerField(default='')
    fit_price = models.PositiveIntegerField(default='')
    program_price = models.PositiveIntegerField(default='')
    machine_price = models.PositiveIntegerField(default='')
    bench_price = models.PositiveIntegerField(default='')
    assembly_price = models.PositiveIntegerField(default='')
    shipping_price = models.PositiveIntegerField(default='')
    laser_price = models.PositiveIntegerField(default='')
    inspect_price = models.PositiveIntegerField(default='')
    total_price = models.PositiveIntegerField(default='')
    quote_id = models.ForeignKey(QuoteLm, default=1, on_delete=models.SET_DEFAULT)


class SearchQuote(models.Model):
    # customer variables
    NONE = ''
    BOEING_CANADA = 'Boeing Canada'
    BOEING_SEATTLE = 'Boeing Seattle'
    BOEING_STLOUIS = 'Boeing St.Louis'
    L3_HARRIS = 'L3 Harris'
    LOCKHEED = 'Lockheed Martin'
    NORTHROP = 'Northrop Grumman'
    SIKORSKY = 'Sikorsky'
    SPIRIT = 'Spirit'

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

    quote_id = models.CharField(
        max_length=30,
        default=NONE,
        blank=True
    )
    customer_id = models.CharField(
        max_length=30,
        choices=CUSTOMER,
        default=NONE,
        blank=True
    )
    date = models.DateField(blank=True)




