# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.SmallIntegerField(choices=[(1, '┅'), (2, '┅┅'), (3, '┅┅┅'), (4, '┅┅┅┅'), (5, '┅┅┅┅┅')]),
        ),
    ]
