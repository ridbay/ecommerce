# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-03 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0033_auto_20200311_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerassignmentemailtemplates',
            name='email_closing',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offerassignmentemailtemplates',
            name='email_greeting',
            field=models.TextField(blank=True, null=True),
        ),
    ]
