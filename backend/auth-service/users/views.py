from .serializers import UserSerializer,UserCreateSerializer
from django.contrib.auth.models import User
from rest_framework import generics

class UserListCreateView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    
    def get_serializer_class(self):
        if self.request.method=="POST":
            return UserCreateSerializer
        return UserSerializer
    
class UserRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer