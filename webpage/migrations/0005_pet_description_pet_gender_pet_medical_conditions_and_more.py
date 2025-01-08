# Generated by Django 4.2.17 on 2024-12-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0004_pet_is_adopted'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pet',
            name='gender',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='medical_conditions',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='pet',
            name='size',
            field=models.TextField(default='male', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='spayed_neutered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pet',
            name='vaccinations',
            field=models.CharField(default='Yes', max_length=100),
            preserve_default=False,
        ),
    ]