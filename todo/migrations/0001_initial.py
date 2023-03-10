# Generated by Django 4.1.1 on 2022-11-07 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=200)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('fechaFinalizacion', models.DateField()),
                ('prioridad', models.IntegerField(default=3)),
            ],
        ),
    ]
