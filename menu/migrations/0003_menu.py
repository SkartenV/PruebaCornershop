# Generated by Django 2.2.3 on 2020-12-12 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0002_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Opcion_1', models.CharField(help_text='Ingrese la Opción 1 del Menú', max_length=200, null=True)),
                ('Opcion_2', models.CharField(help_text='Ingrese la Opción 2 del Menú', max_length=200, null=True)),
                ('Opcion_3', models.CharField(help_text='Ingrese la Opción 3 del Menú', max_length=200, null=True)),
                ('Opcion_4', models.CharField(help_text='Ingrese la Opción 4 del Menú', max_length=200, null=True)),
            ],
        ),
    ]