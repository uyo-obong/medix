from django.db import models


# Create your models here.
class UserTable(models.Model):
    UserStatus = [
        ("pending", "pending"),
        ("verified", "verified"),
        ("approved", "approved"),
        ("deactivated", "deactivated")
    ]

    email = models.CharField(max_length=100, unique=True, db_index=True)
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    mentor = models.BooleanField(default=False)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    # hospital = models.ForeignKey("Hospital", on_delete=models.CASCADE, related_name="users")
    # specialty = models.ForeignKey("Specialty", on_delete=models.CASCADE, related_name="users", null=True)
    # cadre = models.ForeignKey("Cadre", on_delete=models.CASCADE, related_name="users", null=True)
    verification = models.CharField(max_length=250)
    verification_image = models.CharField(max_length=1000)
    avatar = models.TextField()
    cover_image = models.TextField()
    password_hash = models.CharField(max_length=128)
    onboarding_code = models.CharField(max_length=64)
    user_status = models.CharField(
        max_length=20,
        choices=UserStatus,
        default='pending',
    )
    user_hospital_status = models.CharField(
        max_length=20,
        choices=UserStatus,
        default='pending',
    )
    is_admin = models.BooleanField(default=False)
    is_org_admin = models.BooleanField(default=False)
    device_token = models.CharField(max_length=500)
    # push_notification_settings = models.ForeignKey(
    #     "PushNotificationSetting",
    #     on_delete=models.CASCADE,
    #     related_name="user",
    # )
    # email_notification_settings = models.ForeignKey(
    #     "EmailNotificationSetting",
    #     on_delete=models.CASCADE,
    #     related_name="user",
    # )
    username = models.CharField(max_length=100, unique=True, db_index=True, null=True)
    bio = models.CharField(max_length=5000)
    deleted = models.BooleanField(default=False)
    hospital_welcomed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # following = models.ManyToManyField("Case", through="UserCaseFollowing", related_name="followers")
    # visible_cases = models.ManyToManyField("Case", through="UserCaseVisibility", related_name="visible_to")
    # specialties = models.ManyToManyField("Specialty", through="UserSpecialty", related_name="users")
    # facilities = models.ManyToManyField("Facility", through="UserFacility", related_name="users")
    # following_cpd = models.ManyToManyField("Cpd", through="UserCpd", related_name="followers")

    class Meta:
        db_table = "users"
