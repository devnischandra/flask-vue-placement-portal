from flask import request, abort
from extensions import db, cache
from models import User, Company, Student, PlacementDrive, Application

from datetime import datetime, date, timedelta
from api.controllers.company import get_placement_drives_controller

def get_stats_controller():
    total_companies_count = Company.query.filter(Company.status!='rejected').count()
    total_students_count = Student.query.count()
    total_placement_drives_count = PlacementDrive.query.count()
    total_applications_count = Application.query.count()

    return {
        "total_companies_count":total_companies_count,
        "total_students_count":total_students_count,
        "total_placement_drives_count":total_placement_drives_count,
        "total_applications_count":total_applications_count
    }, 200

def get_companies_controller():
    companies = Company.query.all()
    return [
        {
            "id":c.user.id,
            "name":c.user.name,
            "email":c.user.email,
            "is_blacklisted":c.user.is_blacklisted,
            "hr_contact":c.hr_contact,
            "website_url":c.website_url,
            "status":c.status
        } for c in companies
    ], 200

def update_company_controller(company_id):
    company = Company.query.get(company_id)
    data = request.get_json(silent=True) or {}
    
    if company:
        status = data.get("status")
        if status in {"pending", "approved", "rejected"}:
            company.status = status
            db.session.commit()

            cache.delete("admin_companies")
            cache.delete("companies")

            return {"msg": "COMPANY STATUS UPDATED SUCCESSFULLY!"}, 200
    return abort(400)

def get_students_controller():
    students=Student.query.all()
    return [
        {
            "id":s.user.id,
            "name":s.user.name,
            "email":s.user.email,
            "is_blacklisted":s.user.is_blacklisted,
            "gender":s.gender,
            "date_of_birth":datetime.strftime(s.date_of_birth, "%Y-%m-%d"),
            "department":s.department,
            "cgpa":float(s.cgpa),
            "resume_url":s.resume_url
        } for s in students
    ], 200

def update_user_controller(user_id):
    user=User.query.get(user_id)
    data=request.get_json()

    if user:
        if "is_blacklisted" in data:
            user.is_blacklisted=not(user.is_blacklisted)

            if user.is_blacklisted:
                if (user.role == 'student'):
                    for application in user.student.applications:
                        if application.status in ['applied','shortlisted']:
                            application.status = 'cancelled'

                elif user.role == "company":
                    for drive in user.company.placement_drives:
                        today = date.today()
                        drive.end_date = today - timedelta(days=1)
                        for application in drive.applications:
                            if application.status in ["applied", "shortlisted"]:
                                application.status = "cancelled"
                
            db.session.commit()

            cache.delete("admin_companies")
            cache.delete("admin_students")
            cache.delete("companies")

            return {"msg": "BLACKLIST STATUS UPDATED SUCCESSFULLY!"}, 200

    return abort(400)

def get_placement_drives_controller():
    placement_drives=PlacementDrive.query.all()
    return [
        {
            "id":p.id,
            "company_id":p.company_id,
            "company_name":p.company.user.name,
            "job_title":p.job_title,
            "description":p.description,
            "job_mode":p.job_mode,
            "location":p.location,
            "minimum_cgpa":p.minimum_cgpa,
            "start_date":datetime.strftime(p.start_date,"%Y-%m-%d"),
            "end_date":datetime.strftime(p.end_date,"%Y-%m-%d")
        } for p in placement_drives
    ], 200

# to complete -> update end date
def update_placement_drive_controller(placement_drive_id):
    placement_drive=PlacementDrive.query.get(placement_drive_id)
    data=request.get_json()

    if placement_drive and "end_date" in data:
        today=date.today()
        placement_drive.end_date=today-timedelta(days=1)
        db.session.commit()

        cache.delete("admin_placement_drives")

        return {"msg": "PLACEMENT DRIVE UPDATED SUCCESSFULLY!"}, 200
    return abort(400)

def get_applications_controller():
    applications = Application.query.all()
    return[
        {
            "id": a.id,
            "student_id": a.student_id,
            "placement_drive_id": a.placement_drive_id,
            "applied_date": datetime.strftime(a.applied_date, "%Y-%m-%d"),
            "status": a.status,
            "interview_date": datetime.strftime(a.interview_date, "%Y-%m-%d") if (a.interview_date) else None,
            "company_feedback": a.company_feedback,
        } for a in applications
    ], 200


def get_student_controller(student_id):
    student=Student.query.get(student_id)
    if student:
        return {
            "id":student.user.id,
            "name":student.user.name,
            "email":student.user.email,
            "gender":student.gender,
            "date_of_birth":datetime.strftime(student.date_of_birth, "%Y-%m-%d"),
            "department":student.department,
            "cgpa":float(student.cgpa),
            "resume_url":student.resume_url
        }, 200
    return abort(400)