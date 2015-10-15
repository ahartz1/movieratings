# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0012_auto_20151014_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.SmallIntegerField(choices=[(1, 'Under 18'), (18, '18–24'), (25, '25–34'), (35, '35–44'), (45, '45–49'), (50, '50–55'), (56, '56+')]),
        ),
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.CharField(max_length=255, choices=[(0, '"other" or not specified'), (1, 'academic/educator'), (2, 'artist'), (3, 'clerical/admin'), (4, 'college/grad student'), (5, 'customer service'), (6, 'doctor/health care'), (7, 'executive/managerial'), (8, 'farmer'), (9, 'homemaker'), (10, 'K–12 student'), (11, 'lawyer'), (12, 'programmer'), (13, 'retired'), (14, 'sales/marketing'), (15, 'scientist'), (16, 'self-employed'), (17, 'technician/engineer'), (18, 'tradesman/craftsman'), (19, 'unemployed'), (20, 'writer')]),
        ),
    ]
