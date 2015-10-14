# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0010_auto_20151013_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.SmallIntegerField(choices=[(1, 'Under 18'), (18, '18-24'), (25, '25-34'), (35, '35-44'), (45, '45-49'), (50, '50-55'), (56, '56+')]),
        ),
    ]
