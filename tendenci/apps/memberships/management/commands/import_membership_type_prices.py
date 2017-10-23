# -*- coding: utf-8; -*-

from __future__ import absolute_import, unicode_literals

import csv

from django.core.management.base import BaseCommand
from django.db import transaction
from django_countries import countries

from ...models import MembershipType, MembershipTypePriceByCountry


COUNTRIES = {
    'Bahamas, The': 'Bahamas',
    'British Virgin Islands': 'Virgin Islands (British)',
    'Brunei Darussalam': 'Brunei',
    'Channel Islands': 'Channel Islands', #?
    'Congo, Dem. Rep.': 'Congo (the Democratic Republic of the)',
    'Congo, Rep.': 'Congo',
    'Egypt, Arab Rep.': 'Egypt',
    'Gambia, The': 'Gambia',
    'Hong Kong SAR, China': 'Hong Kong',
    'Iran, Islamic Rep.': 'Iran',
    'Korea, Dem. People\'s Rep.': 'North Korea',
    'Korea, Rep.': 'South Korea',
    'Kosovo': 'Kosovo', # ?
    'Kyrgyz Republic': 'Kyrgyzstan',
    'Lao PDR': 'Laos',
    'Macao SAR, China': 'Macao',
    'Macedonia, FYR': 'Macedonia',
    'Micronesia, Fed. Sts.': 'Micronesia (Federated States of)',
    'Russian Federation': 'Russia',
    'Slovak Republic': 'Slovakia',
    'St. Kitts and Nevis': 'Saint Kitts and Nevis',
    'St. Lucia': 'Saint Lucia',
    'St. Martin (French part)': 'Saint Martin (French part)',
    'St. Vincent and the Grenadines': 'Saint Vincent and the Grenadines',
    'Syrian Arab Republic': 'Syria',
    'São Tomé and Principe': 'Sao Tome and Principe',
    'Taiwan, China': 'Taiwan',
    'United States': 'United States of America',
    'Venezuela, RB': 'Venezuela',
    'West Bank and Gaza': 'West Bank and Gaza', # ?
    'Yemen, Rep.': 'Yemen',
}

class Command(BaseCommand):
    help = 'Import a spreadsheet of country-specific prices'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        self.source = csv.DictReader(open(options['filename'], 'r'))

        for index, record in enumerate(self.source):
            country = record['Country'].decode('utf-8')
            category = record['Income'].decode('utf-8')
            price = record['Price']
            renewal_price = record['Renewal']
            admin_fee = record['Admin Fee']
            membership_type = MembershipType.objects.get(name=record['MembershipType'])

            if country in COUNTRIES:
                country = COUNTRIES[country]

            if countries.by_name(country) == '':
                print('Country "{}" not found.'.format(country))
            mtpbc = MembershipTypePriceByCountry.objects.create(
                membership_type=membership_type,
                country=country,
                category=category,
                price=price,
                renewal_price=renewal_price,
                admin_fee=admin_fee)
