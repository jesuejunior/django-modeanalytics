# Generated by Django 3.0.4 on 2020-04-23 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modeanalytics', '0003_auto_20200319_0226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modereportmodel',
            name='space',
        ),
    ]
