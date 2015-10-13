# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0006_auto_20151012_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.TextField(max_length=511, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 12, 19, 55, 48, 511281, tzinfo=utc)),
        ),
    ]
