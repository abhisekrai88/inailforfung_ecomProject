# Generated by Django 3.1.5 on 2021-02-17 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slots', '0001_initial'),
        ('booking', '0006_auto_20210208_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='slots.slots', verbose_name='Time of Booking'),
        ),
    ]
