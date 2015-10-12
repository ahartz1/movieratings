# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import lensview.models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0003_auto_20151010_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 12, 19, 28, 8, 190738, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.SmallIntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], validators=[lensview.models.is_valid_stars]),
        ),
    ]
