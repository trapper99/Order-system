from ___future___ import unicode_literals, absolute_import
from .celery import app as celery_app

__all__ = [
    'celery_app',
]