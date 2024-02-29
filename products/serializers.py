from rest_framework import serializers
from django.db.models import Count

from .models import Product, Lesson, User

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    students_count = serializers.SerializerMethodField()
    average_group_fill_percentage = serializers.SerializerMethodField()
    acquisition_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
    def get_lessons_count(self, obj):
        return Lesson.objects.filter(product=obj).count()
    
    def get_students_count(self, obj):
        return obj.accesses.values('user').distinct().count()

    def get_average_group_fill_percentage(self, obj):
        groups = obj.groups.annotate(user_count=Count('users'))
        if not groups:
            return 0  
        
        total_percentage = 0
        for group in groups:
            fill_percentage = (group.user_count / obj.max_group_size) * 100 if obj.max_group_size > 0 else 0
            total_percentage += fill_percentage
        
        average_percentage = total_percentage / len(groups)
        return round(average_percentage, 2)

    def get_acquisition_percentage(self, obj):
        total_users = User.objects.count()
        users_with_access = obj.accesses.values('user').distinct().count()
        
        if total_users > 0:
            return round((users_with_access / total_users) * 100, 2)
        return 0