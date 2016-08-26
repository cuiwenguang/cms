# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_user', models.CharField(max_length=50)),
                ('to_user', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notification_type', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=500)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
    ]
