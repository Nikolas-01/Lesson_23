# Generated by Django 3.0.5 on 2020-05-18 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0008_auto_20200518_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poet',
            name='poet_dictionary',
        ),
        migrations.DeleteModel(
            name='AnalyticsInfo',
        ),
    ]
