from django.urls import path
from .views import CustomUserView

urlpatterns = [
    path('user/register/', CustomUserView.as_view(), name='create-user')
]