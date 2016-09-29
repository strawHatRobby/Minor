# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-29 10:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(default='')),
                ('correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(default='')),
                ('file', models.FileField(null=True, upload_to=b'')),
                ('marks', models.IntegerField(default=0)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('submission_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('marks', models.IntegerField(default=0)),
                ('order', models.IntegerField(default=0)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.Assignment')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.Question'),
        ),
    ]
