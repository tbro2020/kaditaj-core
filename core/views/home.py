from django.utils.translation import gettext as _
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from core.models import Widget
from datetime import date



class Home(LoginRequiredMixin, View):
    today = date.today()

    def get(self, request):
        permissions = request.user.get_all_permissions()
        permissions = [permission.split('.')[-1] for permission in permissions]
        widgets = Widget.objects.filter(permissions__codename__in=permissions).distinct().order_by('id')
        return render(request, "home.html", {'widgets': widgets})