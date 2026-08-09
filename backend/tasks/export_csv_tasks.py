from celery_app import celery
from models import Student, Company
import csv

@celery.task()
def student_applications(student_id):
    from app import app
    with app.app_context():
        student = Student.query.get(student_id)
        if student:
            applications = student.applications
            filename=f'student_id_{student.id}_applications.csv'
            with open(filename,'w',newline="") as f:
                writer = csv.writer(f)

                writer.writerow([
                    'Application_ID',
                    'Drive_ID',
                    'Company_Name',
                    'Job_Title',
                    'Applied_Date',
                    'Status'
                ])

                for application in applications:

                    writer.writerow([
                        application.id,
                        application.placement_drive_id,
                        application.placement_drive.company.user.name,
                        application.placement_drive.job_title,
                        application.applied_date,
                        application.status
                    ])

            print(f"Student CSV generated: {filename}")            
            return filename

@celery.task()
def company_applications(company_id):
    from app import app
    with app.app_context():
        company = Company.query.get(company_id)
        if company:
            applications = [
                application
                for placement_drive in company.placement_drives
                for application in placement_drive.applications
            ]
            filename=f'company_id_{company_id}_applications.csv'
            with open(filename,'w',newline="") as f:
                writer = csv.writer(f)

                writer.writerow([
                    'Application_ID',
                    'Drive_ID',
                    'Student_ID',
                    'Student_Name',
                    'Applied_Date',
                    'Status'
                ])

                for application in applications:

                    writer.writerow([
                        application.id,
                        application.placement_drive_id,
                        application.student_id,
                        application.student.user.name,
                        application.applied_date,
                        application.status
                    ])

            print(f"Company CSV generated: {filename}")
            return filename
