# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0002_videofile_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videofile',
            name='filename',
            field=models.CharField(max_length=120),
            preserve_default=True,
        ),
    ]
