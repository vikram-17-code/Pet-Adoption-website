# Generated by Django 4.2.17 on 2025-01-05 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0007_alter_pet_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='vaccinations',
            field=models.BooleanField(default=False),
        ),
    ]