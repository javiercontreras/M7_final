# Generated by Django 5.1.3 on 2024-11-25 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmueble',
            old_name='precio_mensual',
            new_name='precio',
        ),
    ]