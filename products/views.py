from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from .models import Product, Lesson
from .serializers import ProductSerializer, LessonSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        product_id = self.request.query_params.get('product_id')
        
        if product_id:
            product = get_object_or_404(Product, pk=product_id)
            if product.accesses.filter(user=user).exists():
                return Lesson.objects.filter(product_id=product_id)
            else:
                raise PermissionDenied("У вас нет доступа к урокам этого продукта.")
        else:
            raise PermissionDenied("Необходимо указать product_id.")