# Generated by Django 4.0.5 on 2022-09-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomapp', '0022_alter_booked_number_of_days_alter_customer_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.CharField(default='#HO19RD', max_length=255),
        ),
        migrations.AlterField(
            model_name='non_room_user',
            name='order_id',
            field=models.CharField(default='#L2JE9G', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='#6NL31O', max_length=255, unique=True),
        ),
    ]