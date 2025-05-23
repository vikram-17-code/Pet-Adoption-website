# Generated by Django 4.2.17 on 2025-01-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0019_alter_pet_gender_alter_pet_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoption',
            name='approval',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='adoption',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, max_length=10),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
