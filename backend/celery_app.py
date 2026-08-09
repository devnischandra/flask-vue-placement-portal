from celery import Celery
import os
from celery.schedules import crontab

# from models import User

celery = Celery(
    "placement_portal",
    broker=os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0"),
    backend=os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0"),
    include=[
        "tasks.interview_tasks",
        "tasks.report_tasks",
        "tasks.export_csv_tasks"
    ]
)

celery.conf.beat_schedule = {
    "send-interview-reminders-daily": {
        "task": "tasks.interview_tasks.send_interview_reminders",
        "schedule": crontab(hour=5,minute=0)
    },
}

celery.conf.beat_schedule = {
    "generate-company-monthly-report": {
        "task": "tasks.report_tasks.generate_company_monthly_report",
        "schedule": crontab(day_of_month=1, hour=5, minute=0)
    }
}    

# @celery.task
# def test_task():
#     with app.app_context():
#         users = User.query.count()
#         print(f"Number of users: {users}")
#         return users