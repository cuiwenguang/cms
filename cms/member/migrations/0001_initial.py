# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
                ('user_name', models.IntegerField(max_length=50, null=True, blank=True)),
                ('article_id', models.IntegerField()),
                ('collect_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pya_pwd', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50, null=True, blank=True)),
                ('avatar', models.CharField(max_length=255)),
                ('job', models.CharField(max_length=50, null=True, blank=True)),
                ('mobile', models.CharField(max_length=20, null=True, blank=True)),
                ('integral', models.IntegerField(default=0)),
                ('paypal', models.CharField(max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
                ('user_name', models.IntegerField(max_length=50, null=True, blank=True)),
                ('channel_id', models.IntegerField()),
                ('channel_name', models.CharField(max_length=50)),
            ],
        ),
    ]
