import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')

app = Celery("school")
# vamos a cargar la informacion de celery en django
app.config_from_object('django.conf:settings', namespace="CELERY")

# Va buscar los archivos que tengan el @app.task
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(self.request)
