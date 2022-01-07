from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Item(models.Model):
    ITEM_STATUS = (
        ('rented','Rented'),
        ('available','Available'),
        ('missing','Missing'),
    )
    university_number   = models.CharField(max_length=2, null=True)
    building_number     = models.CharField(max_length=2, null=True)
    faculty_number      = models.CharField(max_length=2, null=True)
    room_number         = models.CharField(max_length=3, null=True)
    item_number         = models.CharField(max_length=3, unique=True)
    description         = models.CharField(max_length=50)
    status              = models.CharField(choices=ITEM_STATUS, default='available', max_length=30)
    rented_by           = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk}'

    def get_absolute_url(self):
        return reverse("items:items-detail", kwargs={"pk": self.pk})
    

class ItemRent(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rent_date = models.DateTimeField(name='rent_date')
    return_date = models.DateTimeField(name='return_date', null=True, blank=True)
    is_archived = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("items:rents-list")

