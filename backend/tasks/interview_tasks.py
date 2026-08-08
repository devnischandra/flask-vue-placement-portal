from datetime import date, timedelta

from celery_app import celery
from app import app

from models import Application
from extensions import mail
from flask_mail import Message

@celery.task
def send_interview_reminders():
    with app.app_context():
        tomorrow=date.today()+timedelta(days=1)

        applications=Application.query.filter_by(interview_date=tomorrow,status='shortlisted').all()
        for application in applications:
            student = application.student
            msg=Message(
                subject='Interview Reminder',
                recipients=[student.user.email],
                body=f'Reminder For Interview which is on {application.interview_date}!'
            )
            mail.send(msg)
            print(f'Interview reminder sent to {student.user.email} for {application.interview_date}')
        return len(applications)