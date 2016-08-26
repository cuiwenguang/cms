# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20160819_1640'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favorite',
        ),
        migrations.DeleteModel(
            name='Subscribe',
        ),
    ]
