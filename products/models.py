from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_products')
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    min_group_size = models.IntegerField()
    max_group_size = models.IntegerField()

    def __str__(self):
        return self.name

class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.title

class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_accesses')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='accesses')
    access_granted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s access to {self.product.name}"

class Group(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='groups')
    users = models.ManyToManyField(User, related_name='user_groups')
    
    def __str__(self):
        return self.name
