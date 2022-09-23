# Generated by Django 4.0.5 on 2022-09-23 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roomapp', '0007_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.CharField(default='#RH4SES', max_length=255),
        ),
        migrations.CreateModel(
            name='Customer_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(default=True)),
                ('checkout', models.CharField(default='stay', max_length=255)),
                ('bookd_roooms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roomapp.booked')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Ch_out',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaing_balance', models.FloatField(default=0, null=True)),
                ('room_bill', models.FloatField(default=0, null=True)),
                ('resturent_discount', models.FloatField(blank=True)),
                ('vat', models.BooleanField(default=False)),
                ('room_discount', models.FloatField(blank=True)),
                ('remarks', models.CharField(blank=True, max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roomapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Advance_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Advance_amount', models.CharField(blank=True, max_length=255)),
                ('payment_day', models.DateTimeField(auto_now_add=True)),
                ('payment_mode', models.CharField(choices=[('Esewa', 'Eswa'), ('Khalti', 'Khalti'), ('Bank Transfer', 'Bank Transfer'), ('Cash', 'Cash'), ('Other', 'Other')], default='available', max_length=255)),
                ('remarks', models.CharField(blank=True, max_length=255)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='roomapp.customer')),
            ],
        ),
    ]