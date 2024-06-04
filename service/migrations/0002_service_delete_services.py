# Generated by Django 5.0.6 on 2024-06-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("service", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
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
        migrations.DeleteModel(
            name="services",
        ),
    ]
