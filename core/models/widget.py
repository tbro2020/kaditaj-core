from django.utils.translation import gettext as _
from django.db import models

from core.models.fields import AceField, ModelSelect2Multiple
from django.template import Context, Template
from core.models import Base

from crispy_forms.layout import Layout, Row, Column


class Widget(Base):
    description = models.CharField(verbose_name=_('description'), max_length=250)
    name = models.CharField(verbose_name=_('nom'), max_length=100)

    is_staff = models.BooleanField(verbose_name=_('requis pour le personnel'), default=False)
    permissions = ModelSelect2Multiple('auth.permission', verbose_name=_('permissions'))

    template = AceField(mode='html', verbose_name=_('template'))
    view = AceField(mode='python', verbose_name=_('view'))

    list_display = ('id', 'name', 'description', 'updated_at')
    layout = Layout(
        Row(
            Column('name'),
            Column('description'),
        ),
        Row(
            Column('permissions'),
            Column('is_staff'),
        ),
        Row(
            Column('template'),
            Column('view'),
        ),
    )

    def render(self):
        template = Template(self.template)
        exec(self.view, globals(), locals())
        return template.render(Context(locals()))

    class Meta:
        verbose_name = _('widget')
        verbose_name_plural = _('widgets')