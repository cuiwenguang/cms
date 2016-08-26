# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20160818_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
                ('follow_id', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='language',
            field=models.CharField(default=b'en', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile_code',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
