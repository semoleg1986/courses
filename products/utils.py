from django.db import models
from .models import Group

def distribute_user_to_group(user, product):
    group = product.groups.annotate(user_count=models.Count('users')).order_by('user_count').filter(user_count__lt=product.max_group_size).first()
    if not group:
        group = Group.objects.create(name=f"Group for {product.name}", product=product)
    group.users.add(user)
