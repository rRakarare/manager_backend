# Generated by Django 3.2 on 2021-06-01 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_client_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='short',
            field=models.CharField(default='none', max_length=5),
        ),
    ]
