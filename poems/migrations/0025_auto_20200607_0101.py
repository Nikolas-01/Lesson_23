# Generated by Django 3.0.6 on 2020-06-07 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0024_auto_20200607_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstline',
            name='poem',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='firstline', to='poems.Poem'),
        ),
    ]
