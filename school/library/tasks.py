from celery import shared_task
import time

@shared_task
def send_book(name, email):
    time.sleep(20)
    print(name, email)
