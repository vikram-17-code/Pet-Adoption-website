# Generated by Django 5.1.4 on 2025-01-07 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0015_adoption_city_adoption_declaration_adoption_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='breed',
            name='Guard_dog',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='breed',
            name='athletic',
            field=models.BooleanField(default=False),
        ),
    ]
