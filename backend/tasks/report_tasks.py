from celery_app import celery
from models import Company
from extensions import mail
from flask_mail import Message

@celery.task()
def generate_company_monthly_report():
    from app import app
    with app.app_context():
        companies=Company.query.all()

        for company in companies:
            total_placement_drives = len(company.placement_drives)
            applications= [
                application
                for placement_drive in company.placement_drives
                for application in placement_drive.applications
            ]
            total_applications = len(applications)
            total_selected_applications = sum(
                application.status=='selected'
                for application in applications
            )
            placement_ratio=(
                round((total_selected_applications/total_applications)*100, 2)
                if total_applications > 0
                else 0
            )

            report = f"""<html>
            <head><title>Report</title>
            </head>
            <body>
            <p>Total Placement Drives = {total_placement_drives}</p>
            <p>Total Applications = {total_applications}</p> 
            <p>Total Selected Applications = {total_selected_applications}</p> 
            <p>Placement Ratio = {placement_ratio}</p>  
            </body>
            </html>
            """

            filename=f'company_id#{company.id}_report.html'

            with open(filename,'w') as f:
                f.write(report)

            print(f"Report generated: {filename}")

            msg=Message(
                "Check Your Monthly Report!",
                recipients=[company.user.email],
                body='Your Report is attached in HTML Form!'
            )

            with open(filename, "rb") as report_file:
                msg.attach(
                    filename=filename,
                    content_type="text/html",
                    data=report_file.read(),
                )

            mail.send(msg)

        return len(companies)
