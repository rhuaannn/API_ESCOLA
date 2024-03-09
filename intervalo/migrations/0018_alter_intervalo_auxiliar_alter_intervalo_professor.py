# Generated by Django 5.0.2 on 2024-03-09 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auxiliar', '0001_initial'),
        ('intervalo', '0017_alter_intervalo_auxiliar'),
        ('professor', '0003_alter_professor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervalo',
            name='auxiliar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intervalos', to='auxiliar.auxiliar'),
        ),
        migrations.AlterField(
            model_name='intervalo',
            name='professor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intervalos', to='professor.professor'),
        ),
    ]
