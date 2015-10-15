# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0013_auto_20151015_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='num_raters',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
