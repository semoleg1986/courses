from django.db import transaction
from django.db.models import Count
from django.utils import timezone

from .models import Group  

def redistribute_users_among_groups(product):
    with transaction.atomic():
        groups = list(product.groups.annotate(user_count=Count('users')).order_by('user_count'))
        total_users = sum(group.user_count for group in groups) + 1 

        required_groups = max(len(groups), -(-total_users // product.max_group_size))
        users_per_group, extra_users = divmod(total_users, required_groups)

        all_users = [user for group in groups for user in group.users.all()]

        for group in groups:
            group.users.clear()

        user_index = 0
        for i in range(required_groups):
            if i >= len(groups):
                group = Group.objects.create(name=f"Group {i+1} for {product.name}", product=product)
            else:
                group = groups[i]

            for _ in range(users_per_group + (1 if i < extra_users else 0)):
                if user_index < len(all_users):
                    group.users.add(all_users[user_index])
                    user_index += 1
        if user_index < len(all_users):
            groups[-1].users.add(all_users[-1])

def distribute_user_to_group(user, product):
    groups = product.groups.annotate(user_count=Count('users'))
    full_groups = groups.filter(user_count__gte=product.max_group_size).count()

    if not groups.exists():
        new_group = Group.objects.create(name=f"New Group for {product.name}", product=product)
        new_group.users.add(user)
    elif full_groups == groups.count():
        redistribute_users_among_groups(product)
    else:
        group_with_least_users = groups.order_by('user_count').first()
        group_with_least_users.users.add(user)
