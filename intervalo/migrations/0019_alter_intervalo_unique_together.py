# Generated by Django 5.0.2 on 2024-03-16 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intervalo', '0018_alter_intervalo_auxiliar_alter_intervalo_professor'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='intervalo',
            unique_together={('almoco', 'retorno_almoco')},
        ),
    ]
