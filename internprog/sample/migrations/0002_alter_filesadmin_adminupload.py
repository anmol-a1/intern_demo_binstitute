# Generated by Django 4.0 on 2022-01-01 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesadmin',
            name='adminupload',
            field=models.ImageField(upload_to='media'),
        ),
    ]