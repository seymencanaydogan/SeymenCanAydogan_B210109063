# Generated by Django 4.1.2 on 2022-12-25 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contactformmessage_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmessage',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contactformmessage',
            name='message',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contactformmessage',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contactformmessage',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
