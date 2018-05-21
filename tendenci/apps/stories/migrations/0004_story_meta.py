# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0002_custommeta'),
        ('stories', '0003_auto_20180315_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='meta',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='meta.Meta'),
        ),
    ]
