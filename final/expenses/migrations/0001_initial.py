# Generated by Django 4.0.7 on 2022-10-28 19:37

import datetime
from django.db import migrations, models
import expenses.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
                ('amount', models.IntegerField()),
                ('comments', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to=expenses.models.upload_path)),
                ('approval', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
            ],
        ),
    ]
