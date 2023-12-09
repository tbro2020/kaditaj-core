from dal.autocomplete import ModelSelect2
from django.urls import reverse_lazy
from django.db import models


class ModelSelect2Single(models.OneToOneField):
    def formfield(self, **kwargs):
        to_field = getattr(self, 'foreign_related_fields', None)
        to_field = to_field[0].name if to_field else 'pk'
        kwargs['widget'] = ModelSelect2(url=reverse_lazy('api:autocomplete', kwargs={
            'to_field': to_field,
            'app': self.remote_field.model._meta.app_label,
            'model': self.remote_field.model._meta.model_name
        }), attrs = {
            'data-minimum-input-length': 2,
            'data-theme': 'bootstrap-5'
        })
        return super().formfield(**kwargs)