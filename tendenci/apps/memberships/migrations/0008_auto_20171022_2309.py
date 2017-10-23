# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0007_membershiptypepricebycountry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membershiptypepricebycountry',
            options={'verbose_name_plural': 'Membership prices by country'},
        ),
        migrations.AddField(
            model_name='membershiptypepricebycountry',
            name='category',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
