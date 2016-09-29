# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-29 10:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255, unique=True)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(default=datetime.datetime.now)),
                ('credits', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(default='')),
                ('syllabus', models.FileField(null=True, upload_to=b'')),
                ('credits', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
    ]
