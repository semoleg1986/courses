from rest_framework import serializers
from .models import Product, Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
    def get_lessons_count(self, obj):
        return Lesson.objects.filter(product=obj).count()