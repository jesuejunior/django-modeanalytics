# Generated by Django 3.0.4 on 2020-03-19 02:26

import django.contrib.postgres.fields.jsonb
from django.db import migrations

import modeanalytics.models


class Migration(migrations.Migration):

    dependencies = [
        ('modeanalytics', '0002_auto_20200317_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modereportmodel',
            name='params',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=modeanalytics.models.f, help_text='Choices are Select([ ]), Multiselect([ [ ] ]), Text and Date(YYYY-MM-DD)', null=True, verbose_name='Query Parameters(JSON)'),
        ),
    ]
