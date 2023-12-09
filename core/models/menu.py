from .fields import ModelSelect2Multiple, ChoiceField
from django.utils.translation import gettext as _
from django.contrib.staticfiles import finders
from django.db import models
from .base import Base
import glob

from django.contrib.contenttypes.models import ContentType
from crispy_forms.layout import Layout, Row, Column


ICONS = glob.glob('{}/*svg'.format(finders.find('ICONS')))

class Menu(Base):
    ICONS = [((icon.split('/')[-1]).split('.')[0], ' '.join(((icon.split('/')[-1]).split('.')[0]).split('-')).title()) for icon in ICONS]

    icon = ChoiceField(verbose_name=_('icon'), choices=ICONS, max_length=100, null=True, default=None)
    name = models.CharField(verbose_name=_('nom'), max_length=100, unique=True)
    children = ModelSelect2Multiple(ContentType, verbose_name=_('sous-menu'))
    
    layout = Layout(Row(Column('icon'), Column('name')), 'children')
    list_display = ('id', 'name', 'updated_at')
    search_fields = ('id', 'name')
    
    class Meta:
        verbose_name = _('menu')
        verbose_name_plural = _('menus')