# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('X', 'Did not answer')])),
                ('occupation', models.CharField(max_length=40)),
                ('zipcode', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('stars', models.PositiveSmallIntegerField()),
                ('movie', models.ForeignKey(to='lensview.Movie')),
                ('rater', models.ForeignKey(to='lensview.Rater')),
            ],
        ),
    ]
