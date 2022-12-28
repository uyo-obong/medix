# Generated by Django 4.1.4 on 2022-12-28 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Images",
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
                ("image", models.FileField(upload_to="images/")),
            ],
        ),
        migrations.CreateModel(
            name="GestationalTable",
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
                ("age", models.IntegerField()),
                (
                    "medical_history",
                    models.CharField(
                        choices=[
                            ("True", "True"),
                            ("False", "False"),
                            ("Others", "Others"),
                        ],
                        default="True",
                        max_length=20,
                    ),
                ),
                ("documents", models.TextField(blank=True, max_length=100, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("True", "True"),
                            ("False", "False"),
                            ("Others", "Others"),
                        ],
                        default="True",
                        max_length=20,
                    ),
                ),
                ("volunteer_health", models.BooleanField(default=True)),
                ("height", models.FloatField(default=0.0)),
                (
                    "unit_of_height",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("weight", models.FloatField(default=0.0)),
                (
                    "unit_of_weight",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("temperature", models.FloatField(default=0.0)),
                (
                    "unit_of_temperature",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "blood_pressure",
                    models.FloatField(blank=True, max_length=100, null=True),
                ),
                (
                    "unit_of_blood_pressure",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "images",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="users",
                        to="new_feature.images",
                    ),
                ),
            ],
            options={
                "db_table": "gestation",
            },
        ),
    ]