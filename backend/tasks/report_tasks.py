from celery_app import celery
from app import app
from models import Company, Application

@celery.task()
def generate_company_monthly_report():
    with app.app_context():
        companies=Company.query.all()
        applications=Application.query.all()

        for company in companies:
            total_placement_drives = len(company.placement_drives)
            total_applications = len(applications)
            total_selected_applications = sum(
                application.status=='selected'
                for application in applications
            )
            placement_ratio=round((total_selected_applications/total_applications)*100, 2)

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
        return len(companies)
            

            