# Generated by Django 3.2.5 on 2021-12-27 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_rename_return_date_itemrent_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemrent',
            name='return_date',
            field=models.DateTimeField(null=True),
        ),
    ]