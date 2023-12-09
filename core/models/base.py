from django_currentuser.db.models import CurrentUserField
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

from core.models.fields import JSONField
from django.conf import settings
from django.db import models
from django.apps import apps
from pydoc import locate

BASE_MANAGER = getattr(settings, 'CORE_BASE_MODEL_QUERYSET', 'django.db.models.QuerySet')
BASE_MANAGER = locate(BASE_MANAGER).as_manager()

class Base(models.Model):
    updated_by = CurrentUserField(verbose_name=_('mis à jour par') ,related_name='%(app_label)s_%(class)s_updated_by', on_update=True)
    created_by = CurrentUserField(verbose_name=_('créé par') ,related_name='%(app_label)s_%(class)s_created_by')

    created_at = models.DateTimeField(verbose_name=_('créé le/à'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('mis à jour le/à'), auto_now=True)

    metadata = JSONField(verbose_name=_('meta'), default=dict, blank=True)
    objects = BASE_MANAGER

    list_display = ('id', 'name')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('core:change', args=[self._meta.app_label, self._meta.model_name, self.pk])
    
    @property
    def template(self):
        Template = apps.get_model('core', model_name='template')
        return Template.objects.filter(content_type__model=self._meta.model_name).first()
    
    class Meta:
        abstract = True