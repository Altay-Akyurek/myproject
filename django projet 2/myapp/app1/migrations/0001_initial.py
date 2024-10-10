# Generated by Django 5.0.2 on 2024-10-04 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Register",
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
                ("firs_name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=128)),
            ],
        ),
    ]
