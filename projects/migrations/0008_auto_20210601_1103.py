# Generated by Django 3.2 on 2021-06-01 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20210601_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttype',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='projecttype',
            name='short',
            field=models.CharField(max_length=4, unique=True),
        ),
    ]
