# Generated by Django 4.2.6 on 2023-10-13 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='nombre_d_animaux_de_compagnie',
        ),
        migrations.AddField(
            model_name='person',
            name='official_homepage',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('J', 'Journal'), ('T', 'Technologie'), ('P', 'Politique'), ('E', 'Economique')], default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date_de_publication',
            field=models.DateField(default=datetime.datetime(2023, 10, 13, 17, 40, 29, 608809)),
        ),
    ]
