# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20160124_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corda',
            name='id',
        ),
        migrations.RemoveField(
            model_name='exame',
            name='id',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='id',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='id',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='id',
        ),
        migrations.AddField(
            model_name='exame',
            name='nome',
            field=models.CharField(default=b'', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='corda',
            name='cor',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='nome',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='turma',
            name='nome',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
