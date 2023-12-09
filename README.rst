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

2. Include the polls URLconf in your project urls.py like this::

    path("core/", include("core.urls")),

3. Run ``python manage.py migrate`` to create the polls models.

4. Visit http://127.0.0.1:8000/core/ to participate in the poll.