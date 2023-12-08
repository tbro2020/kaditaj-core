from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from core.views import BaseView

import xlsxwriter
from io import BytesIO

class Template(BaseView):
    def get(self, request, pk):
        obj = get_object_or_404(ContentType, pk=pk)
        model = obj.model_class()

        fields = getattr(model, 'layout', None)
        if not fields:
            messages.error(request, 'Aucun layout n\'est défini pour ce modèle.')
            return redirect(request.META.get('HTTP_REFERER'))
        
        fields = [field.name for field in fields.get_field_names()]
        fields = {field:model._meta.get_field(field) for field in fields 
                  if model._meta.get_field(field).get_internal_type() not in ['FileField', 'ImageField']}
        
        #fields = {k:v for k, v in fields.items()}
        output = BytesIO()

        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        for index, column in enumerate(fields.keys()):
            worksheet.write(0, index, column)

        workbook.close()
        output.seek(0)

        response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = "attachment; filename={}.xlsx".format(model._meta.verbose_name_plural)
        
        return response

