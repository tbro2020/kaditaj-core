from crispy_forms.layout import Layout, Column, Row
from django.utils.translation import gettext as _
from core.utils import upload_directory_file
from django.db import models
from .base import Base


default_logo = lambda: "assets/images/logo/logo.svg"

class Organization(Base):
    logo = models.ImageField(verbose_name=_('logo'), upload_to=upload_directory_file, default=default_logo())
    name = models.CharField(verbose_name=_('nom'), max_length=100)

    list_display = ('id', 'name')
    layout = Layout(Row(Column('logo'), Column('name')))
    
    def save(self, *args, **kwargs):
        if self.__class__.objects.exists():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('organization')
        verbose_name_plural = _('organizations')