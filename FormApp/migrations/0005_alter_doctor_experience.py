# Generated by Django 4.2.7 on 2024-03-20 16:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("FormApp", "0004_alter_doctor_address_alter_doctor_experience_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="experience",
            field=models.IntegerField(),
        ),
    ]
