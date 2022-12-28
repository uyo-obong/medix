# Generated by Django 4.1.4 on 2022-12-28 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserTable",
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
                ("email", models.CharField(db_index=True, max_length=100, unique=True)),
                ("title", models.CharField(max_length=100)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("job_title", models.CharField(max_length=100)),
                ("image", models.CharField(max_length=1000)),
                ("mentor", models.BooleanField(default=False)),
                ("country", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
                ("verification", models.CharField(max_length=250)),
                ("verification_image", models.CharField(max_length=1000)),
                ("avatar", models.TextField()),
                ("cover_image", models.TextField()),
                ("password_hash", models.CharField(max_length=128)),
                ("onboarding_code", models.CharField(max_length=64)),
                (
                    "user_status",
                    models.CharField(
                        choices=[
                            ("pending", "pending"),
                            ("verified", "verified"),
                            ("approved", "approved"),
                            ("deactivated", "deactivated"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "user_hospital_status",
                    models.CharField(
                        choices=[
                            ("pending", "pending"),
                            ("verified", "verified"),
                            ("approved", "approved"),
                            ("deactivated", "deactivated"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("is_admin", models.BooleanField(default=False)),
                ("is_org_admin", models.BooleanField(default=False)),
                ("device_token", models.CharField(max_length=500)),
                (
                    "username",
                    models.CharField(
                        db_index=True, max_length=100, null=True, unique=True
                    ),
                ),
                ("bio", models.CharField(max_length=5000)),
                ("deleted", models.BooleanField(default=False)),
                ("hospital_welcomed", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "users",
            },
        ),
    ]