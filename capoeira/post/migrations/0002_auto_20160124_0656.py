# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('complemento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('mestre_examinador', models.CharField(max_length=100)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequencia_corda', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('rg', models.CharField(max_length=20)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(max_length=50)),
                ('profissao', models.CharField(max_length=50)),
                ('grau_escolar', models.CharField(max_length=50)),
                ('cor_corda', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('turno', models.CharField(max_length=100)),
                ('horario', models.DateField()),
                ('dia_semana', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.Pessoa')),
                ('pai', models.CharField(max_length=100)),
                ('mae', models.CharField(max_length=100)),
            ],
            bases=('post.pessoa',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.Pessoa')),
                ('registro', models.CharField(max_length=100)),
            ],
            bases=('post.pessoa',),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Endereco'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Grupo'),
        ),
        migrations.AddField(
            model_name='exame',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Turma'),
        ),
        migrations.AddField(
            model_name='turma',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Aluno'),
        ),
        migrations.AddField(
            model_name='turma',
            name='professor',
            field=models.ManyToManyField(to='post.Professor'),
        ),
    ]
