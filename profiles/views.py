from rest_framework.generics import CreateAPIView
from .serializers import CustomUserSerializer

class CustomUserView(CreateAPIView):
    serializer_class = CustomUserSerializer