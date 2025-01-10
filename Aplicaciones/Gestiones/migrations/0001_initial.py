# Generated by Django 5.1.3 on 2025-01-09 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campistas',
            fields=[
                ('id_camp', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_camp', models.CharField(max_length=100)),
                ('apell_camp', models.CharField(max_length=100)),
                ('correo_camp', models.EmailField(max_length=254)),
                ('telef_camp', models.CharField(max_length=10)),
                ('cedula_camp', models.CharField(max_length=10)),
                ('direcc_camp', models.TextField()),
            ],
        ),
    ]
