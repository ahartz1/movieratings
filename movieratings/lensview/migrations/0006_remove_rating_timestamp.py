# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0005_auto_20151007_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='timestamp',
        ),
    ]
