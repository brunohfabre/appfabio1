# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('duration_time', models.DateTimeField(verbose_name='Dura\xe7\xe3o de Jogo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
            options={
                'verbose_name': 'Esporte',
                'verbose_name_plural': 'Esportes',
            },
        ),
    ]