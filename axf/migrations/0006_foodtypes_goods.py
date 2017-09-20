# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0005_mainshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=10)),
                ('typename', models.CharField(max_length=20)),
                ('typesort', models.IntegerField()),
                ('childtypenames', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=10)),
                ('productimg', models.CharField(max_length=150)),
                ('productname', models.CharField(max_length=50)),
                ('productlongname', models.CharField(max_length=100)),
                ('isxf', models.NullBooleanField(default=False)),
                ('pmdesc', models.CharField(max_length=10)),
                ('specifics', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
                ('marketprice', models.CharField(max_length=10)),
                ('categoryid', models.CharField(max_length=10)),
                ('childcid', models.CharField(max_length=10)),
                ('childcidname', models.CharField(max_length=10)),
                ('dealerid', models.CharField(max_length=10)),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
        ),
    ]