# Generated by Django 5.0.6 on 2024-06-01 17:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="services",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("service_icon", models.CharField(max_length=30)),
                ("service_title", models.CharField(max_length=30)),
                ("service_des", models.TextField()),
            ],
        ),
    ]
