from celery import Celery
# from app import app
import os
from celery.schedules import crontab

# from models import User

celery = Celery(
    "placement_portal",
    broker=os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0"),
    backend=os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")
)

from tasks.interview_tasks import send_interview_reminders

celery.conf.beat_schedule = {
    "send-interview-reminders-daily": {
        "task": "tasks.interview_tasks.send_interview_reminders",
        "schedule": crontab(hour=9,minute=0)
    },
}

# @celery.task
# def test_task():
#     with app.app_context():
#         users = User.query.count()
#         print(f"Number of users: {users}")
#         return users