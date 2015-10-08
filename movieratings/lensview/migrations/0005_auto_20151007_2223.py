# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0004_auto_20151007_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(default=datetime.datetime(2015, 10, 7, 22, 22, 6, 782369, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='occupation',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(default='00000', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='timestamp',
            field=models.DateField(default=datetime.datetime(2015, 10, 7, 22, 23, 20, 804251, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
