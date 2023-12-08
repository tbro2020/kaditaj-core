from django.utils.translation import gettext as _
from notifications.signals import notify
from celery import shared_task
from django.apps import apps
import pandas as pd

from core.models import ImporterStatus

@shared_task(name='daily')
def daily():
    qs = apps.get_model('core', 'job').objects.all()
    for obj in qs:
        try:
            exec(obj.job, locals(), globals())
        except:
            pass

@shared_task(name='importer')
def importer(pk):
    model = apps.get_model('core', 'importer')
    obj = model.objects.get(pk=pk)

    if not obj.created_by.has_perm('core.add_{}'.format(obj.content_type.model)):
        obj.status = ImporterStatus.ERROR
        return obj.save()

    obj.status = ImporterStatus.PROCESSING
    obj.save()

    model = obj.content_type.model_class()
    
    df = pd.read_excel(obj.document)
    df = df.where(pd.notnull(df), None)
    df.columns = [col.lower() for col in df.columns]

    try:
        data = df.to_dict(orient='records')
        [row.update({'created_by': obj.created_by}) for row in data]
        data = [model(**row) for row in df.to_dict(orient='records')]
        model.objects.bulk_create(data, ignore_conflicts=True)
    except Exception as e:
        obj.status = ImporterStatus.ERROR
        obj.save()
        return

    # send notification
    obj.status = ImporterStatus.SUCCESS
    obj.save()

    # notify user
    notify.send(**{
        'sender': obj,
        'actor': obj.created_by,
        'recipient': obj.created_by,
        'verb': _('Données importées {}').format(obj.content_type.model),
        'action_object': obj,
        'target': obj,
        'level': 'info',
        'description': _('La tâche d\'importation d(e) {} est terminée').format(obj.content_type.model),
        'public': False,
        'url': obj.get_absolute_url()
    })