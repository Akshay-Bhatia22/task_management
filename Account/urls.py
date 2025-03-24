from django.urls import path

from .views import NewAccount
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('signup', NewAccount.as_view(), name='signup'),
    path('login', TokenObtainPairView.as_view(), name='login'),
]