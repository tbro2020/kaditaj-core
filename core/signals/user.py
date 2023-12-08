from django.db.models.signals import pre_save, pre_delete
from django_keycloak.connector import lazy_keycloak_admin
from django.dispatch import receiver
from core.models import User
import uuid


@receiver(pre_save, sender=User)
def user_created(sender, instance, **kwargs):
    if hasattr(instance, 'keycloak_id') and instance.keycloak_id: return
    instance.keycloak_id = uuid.uuid4()
    employee = instance.employee
    obj = lazy_keycloak_admin.create_user({
        'email': instance.email,
        'username': instance.email,
        'enabled': True, 
        'emailVerified': True, 
        'lastName': getattr(employee, 'last_name', None),
        'firstName': getattr(employee, 'first_name', None), 
        'credentials': [{'value': 'Kinshasa-2021', 'type': 'password', 'temporary': False}]
    })
    
@receiver(pre_delete, sender=User)
def user_deleted(sender, instance, **kwargs):
    lazy_keycloak_admin.delete_user(instance.keycloak_id)