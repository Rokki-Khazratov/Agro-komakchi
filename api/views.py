# from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import *
from .serializers import *

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class NewsIMages(generics.ListCreateAPIView):
    queryset = NewsImage.objects.all()
    serializer_class = NewsImageSerializer

# Представление для получения списка новостей и создания новой новости
class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

# Представление для получения, обновления и удаления конкретной новости
class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]



# List and create view for categories
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Detail view for retrieving, updating, and deleting a specific category
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    

# List and create view for services
class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# Detail view for retrieving, updating, and deleting a specific service
class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer