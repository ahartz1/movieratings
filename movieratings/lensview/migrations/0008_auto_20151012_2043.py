# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0007_auto_20151012_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
