# Generated by Django 4.1.2 on 2022-12-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Policlinic', '0019_alter_appointment_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='ip',
            field=models.CharField(max_length=20),
        ),
    ]
