# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='users.User')),
                ('users', models.ManyToManyField(to='users.User')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
