# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0009_auto_20151013_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(max_length=10),
        ),
    ]
