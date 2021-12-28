# Generated by Django 3.2.5 on 2021-12-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_itemrent_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='is_archived',
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('rented', 'Rented'), ('available', 'Available'), ('missing', 'Missing')], default='available', max_length=30),
        ),
    ]
