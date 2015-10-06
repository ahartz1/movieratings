# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='title',
            new_name='movie',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.AddField(
            model_name='rating',
            name='rater',
            field=models.ForeignKey(to='lensview.Rater', default=0),
            preserve_default=False,
        ),
    ]
