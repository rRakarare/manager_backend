# Generated by Django 3.2 on 2021-06-09 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_remove_client_short'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_of_invoicing',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_of_payment',
            field=models.DateField(blank=True, null=True),
        ),
    ]
