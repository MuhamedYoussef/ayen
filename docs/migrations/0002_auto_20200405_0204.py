# Generated by Django 3.0.5 on 2020-04-05 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='file',
            field=models.FileField(upload_to='media/'),
        ),
    ]
