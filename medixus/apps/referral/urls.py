from django.urls import path
from medixus.apps.referral.views import GetAuth

urlpatterns = [
    path('referral', GetAuth.as_view())
]
