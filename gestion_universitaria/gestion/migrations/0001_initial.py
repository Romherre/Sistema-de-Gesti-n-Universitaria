# Generated by Django 5.0.7 on 2024-07-19 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=10, unique=True)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
