# Generated by Django 4.1.3 on 2023-01-26 20:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_restaurant_comment_comment_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]