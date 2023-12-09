from django.shortcuts import render
from django.apps import apps
from .base import BaseView

#from core.models import Approbation


class ActionRequired(BaseView):
    def get(self, request):
        Approbation = apps.get_model('core', 'approbation')
        return render(request, 'action_required.html', {
            'qs': Approbation.objects.filter(user=request.user, action__isnull=True)
        })