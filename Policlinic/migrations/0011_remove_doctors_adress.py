# Generated by Django 4.1.2 on 2022-12-25 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Policlinic', '0010_doctors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='adress',
        ),
    ]
