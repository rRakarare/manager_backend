# Generated by Django 3.2 on 2021-08-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_invoicenumbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
    ]