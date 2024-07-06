# Generated by Django 5.0.6 on 2024-06-01 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_package_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('booked', 'booked'), ('pending', 'pending'), ('reject', 'reject'), ('paid', 'paid'), ('approved', 'approved')], default='pending', max_length=50),
        ),
    ]