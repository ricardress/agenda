# Generated by Django 4.1.1 on 2022-11-07 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=12)),
                ('correo', models.EmailField(max_length=254)),
                ('empresa', models.CharField(max_length=20)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('notas', models.TextField()),
            ],
        ),
    ]