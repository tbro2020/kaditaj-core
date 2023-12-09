=====
Polls
=====

Core is a Django app to conduct web-based CMS. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add the follows app below defautl django INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        'django.contrib.humanize',
        
        'dal',
        'dal_select2',

        'tinymce',
        'mathfilters',
        'crispy_forms',
        'widget_tweaks',
        'django_filters',
        'rest_framework',
        'crispy_bootstrap5',
        'django_json_widget',

        'qr_code',
        'django_ace',
        'notifications',
        'phonenumber_field',

        'core'
    ]

3. Add context to settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context.base'
            ],
        },
    },
]

4. Add crispy bootstrap pack in settings file

CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

5. Include the polls URLconf in your project urls.py like this::

    path('', include('core.urls')),
    path('', include('django.contrib.auth.urls')),

6. Run ``python manage.py migrate`` to create the polls models.
7. Visit http://127.0.0.1:8000/core/ to participate in the poll.

8. Advance settings

In case you would like to override the default manager to all model based on core.Base parent
in your settings file just override the follow attribute

CORE_BASE_MODEL_QUERYSET = 'app.models.manager.ClassName'