# Generated by Django 5.0.2 on 2024-06-29 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=50)),
                ("author", models.CharField(max_length=50)),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
            ],
        ),
        migrations.CreateModel(
            name="Status",
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
                (
                    "user_status",
                    models.SmallIntegerField(
                        choices=[
                            (1, "Read"),
                            (2, "Want To Read"),
                            (3, "Did Not Finish"),
                            (4, "Reading"),
                        ],
                        default=1,
                    ),
                ),
                ("rating", models.IntegerField()),
                ("review", models.CharField(max_length=5000)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="book_nook.book"
                    ),
                ),
            ],
        ),
    ]
