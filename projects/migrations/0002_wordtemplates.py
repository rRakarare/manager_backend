# Generated by Django 3.2 on 2021-07-21 09:06

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordTemplates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('template', models.FileField(upload_to=projects.models.upload_to_template)),
            ],
        ),
    ]
