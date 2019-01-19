# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-01-17 08:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mei', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('isselect', models.BooleanField(default=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mei.GoodDetail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mei.User')),
            ],
            options={
                'db_table': 'mei_cart',
            },
        ),
    ]
