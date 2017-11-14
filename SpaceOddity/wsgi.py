"""
WSGI config for SpaceOddity project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from whitenoise.django import DjangoWhiteNoise
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SpaceOddity.settings")

application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(application)

