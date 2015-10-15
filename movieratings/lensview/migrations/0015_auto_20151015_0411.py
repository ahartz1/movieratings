# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0014_movie_num_raters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='num_raters',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
