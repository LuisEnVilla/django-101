# Generated by Django 2.2.7 on 2019-11-23 17:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('token', models.CharField(max_length=120)),
                ('blackList', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, size=None)),
            ],
        ),
    ]