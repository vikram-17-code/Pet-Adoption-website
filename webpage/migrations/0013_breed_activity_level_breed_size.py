# Generated by Django 4.2.17 on 2025-01-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0012_breed_first_time_owner_breed_good_with_kids_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='breed',
            name='activity_level',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=10),
        ),
        migrations.AddField(
            model_name='breed',
            name='size',
            field=models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default='medium', max_length=10),
        ),
    ]
