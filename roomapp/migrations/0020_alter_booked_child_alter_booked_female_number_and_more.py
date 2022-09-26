# Generated by Django 4.0.5 on 2022-09-26 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomapp', '0019_alter_booked_child_alter_booked_female_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked',
            name='child',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='booked',
            name='female_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='booked',
            name='male_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='booked',
            name='other_gender',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.CharField(default='#8GF675', max_length=255),
        ),
        migrations.AlterField(
            model_name='non_room_user',
            name='order_id',
            field=models.CharField(default='#VDOEC8', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='#GERAY1', max_length=255, unique=True),
        ),
    ]
