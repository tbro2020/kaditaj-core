from dal.autocomplete import ListSelect2
from django.db import models


class ChoiceField(models.CharField):
    def formfield(self, **kwargs):
        kwargs['widget'] = ListSelect2(attrs={'data-theme': 'bootstrap-5'})
        return super().formfield(**kwargs)