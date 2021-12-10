from django.db import models
from django.conf import settings

class Item(models.Model):
    ITEM_STATUS = (
        ('rented','Rented'),
        ('pending','Pending'),
        ('available','Available'),
        ('missing','Missing'),
    )
    # QR code (or in different class ex. class Code) ex: '01 01 01 315 077'
    university_number   = models.CharField(max_length=2, null=True)
    building_number     = models.CharField(max_length=2, null=True)
    faculty_number      = models.CharField(max_length=2, null=True)
    room_number         = models.CharField(max_length=3, null=True)
    item_number         = models.CharField(max_length=3, unique=True)

    # Info only
    description         = models.CharField(max_length=50)
    status              = models.CharField(choices=ITEM_STATUS, default='available', max_length=30)
    
    rented_by           = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    date_rented         = models.DateTimeField('date rented', null=True)
    date_returned       = models.DateTimeField('date returned', null=True)

    def __str__(self):
        return f'{self.pk}: {self.item_number}'
    