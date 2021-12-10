# Generated by Django 3.2.5 on 2021-12-10 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date_rented',
            field=models.DateTimeField(null=True, verbose_name='date rented'),
        ),
        migrations.AddField(
            model_name='item',
            name='date_returned',
            field=models.DateTimeField(null=True, verbose_name='date returned'),
        ),
        migrations.AddField(
            model_name='item',
            name='rented_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='building_number',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='faculty_number',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='room_number',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='university_number',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
