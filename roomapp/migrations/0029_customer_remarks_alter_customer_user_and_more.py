# Generated by Django 4.0.5 on 2022-11-03 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomapp', '0028_remove_room_final_number_remove_room_intital_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='remarks',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.CharField(default='#K07QQR', max_length=255),
        ),
        migrations.AlterField(
            model_name='non_room_user',
            name='order_id',
            field=models.CharField(default='#APA76M', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='#WXPNDU', max_length=255, unique=True),
        ),
    ]