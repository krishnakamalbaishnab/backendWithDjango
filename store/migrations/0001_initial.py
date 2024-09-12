# Generated by Django 5.1.1 on 2024-09-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("firstName", models.CharField(max_length=255)),
                ("lastName", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(max_length=255)),
                ("birthDate", models.DateTimeField(null=True)),
                (
                    "membership",
                    models.CharField(
                        choices=[("B", "Bronze"), ("S", "Silver"), ("G", "Gold")],
                        default="B",
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("placed_at", models.DateField(auto_now_add=True)),
                (
                    "payment_status",
                    models.CharField(
                        choices=[("P", "Pending"), ("C", "Complete"), ("F", "Failed")],
                        default="P",
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("inventory", models.IntegerField()),
                ("last_update", models.DateField(auto_now=True)),
            ],
        ),
    ]
