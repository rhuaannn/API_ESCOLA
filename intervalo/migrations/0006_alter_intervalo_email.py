# Generated by Django 5.0.2 on 2024-03-05 03:17

import professor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intervalo', '0005_intervalo_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervalo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name=professor.models.Professor),
        ),
    ]
