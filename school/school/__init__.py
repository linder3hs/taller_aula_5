# usamos as para poner una alias
from .celery import app as celery_app

__all__ = ('celery_app',)
