# Generated by Django 3.1.5 on 2021-02-21 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imageFiles', '0007_imagefiles_promotion_id'),
        ('promotion', '0007_auto_20210208_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imageFiles.imagefiles'),
        ),
    ]
