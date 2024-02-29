from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProductAccess, Group
from .utils import distribute_user_to_group

@receiver(post_save, sender=ProductAccess)
def post_save_product_access(sender, instance, created, **kwargs):
    if created:
        distribute_user_to_group(instance.user, instance.product)
