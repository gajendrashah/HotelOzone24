# Generated by Django 4.0.5 on 2022-09-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomapp', '0005_booked_number_of_days_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.CharField(default='#4508T6', max_length=255, unique=True),
        ),
    ]
