# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0006_membershipset_donation_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipTypePriceByCountry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=15, blank=True, help_text='Set 0 for free membership.', verbose_name='Price')),
                ('renewal_price', models.DecimalField(decimal_places=2, default=0, max_digits=15, blank=True, help_text='Set 0 for free membership.', null=True, verbose_name='Renewal Price')),
                ('admin_fee', models.DecimalField(decimal_places=2, default=0, max_digits=15, blank=True, help_text='Admin fee for the first time processing', null=True, verbose_name='Admin Fee')),
                ('membership_type', models.ForeignKey(to='memberships.MembershipType')),
            ],
        ),
    ]
