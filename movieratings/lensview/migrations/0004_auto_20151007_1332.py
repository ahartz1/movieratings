# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0003_auto_20151007_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('X', 'Did not answer')], max_length=1),
        ),
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
