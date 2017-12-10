# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-09 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wiki', '0002_urlpath_moved_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='BSI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UGA',
            fields=[
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='wiki.Article')),
            ],
        ),
        migrations.AddField(
            model_name='bsi',
            name='references',
            field=models.ManyToManyField(blank=True, related_name='is_linked_to', to='bsi.UGA'),
        ),
        migrations.AddField(
            model_name='bsi',
            name='url',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wiki.URLPath'),
        ),
    ]