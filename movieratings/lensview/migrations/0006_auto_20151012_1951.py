# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0005_auto_20151012_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 12, 19, 51, 44, 678598, tzinfo=utc)),
        ),
    ]
