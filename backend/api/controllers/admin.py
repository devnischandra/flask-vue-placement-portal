from flask import request, abort
from extensions import db
from models import User, Company, Student, PlacementDrive, Application

from datetime import datetime, date

def search_controller():
    data=request.args
    user_type=data["user_type"]
    search_query=data["search_query"]
    search_value=data["search_value"]

    column=getattr(User,search_query,None)

    if [user_type,search_query,search_value] and column is not None:

        companies=Company.query.join(User).filter(User.role=="company",column==search_value).all()
        students=Student.query.join(User).filter(User.role=="student",column==search_value).all()

        if user_type=="company" and companies:
            return [
                {
                    "id":c.user.id,
                    "name":c.user.name,
                    "email":c.user.email,
                    "is_blacklisted":c.user.is_blacklisted,
                    "hr_contact":c.hr_contact,
                    "website_url":c.website_url,
                    "is_approved":c.is_approved
                } for c in companies
            ], 200

        if user_type=="student" and students:
            return [
                {
                    "id":s.user.id,
                    "name":s.user.name,
                    "email":s.user.email,
                    "is_blacklisted":s.user.is_blacklisted,
                    "gender":s.gender,
                    "date_of_birth":datetime.strftime(s.date_of_birth, "%d-%m-%Y"),
                    "department":s.department,
                    "cgpa":s.cgpa,
                    "resume_url":s.resume_url,
                    "is_placed":s.is_placed
                } for s in students
            ], 200
            
        return {"msg": "NOT FOUND"}, 404
    
    return abort(400)

def get_stats_controller():
    total_companies_count = Company.query.count()
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
            "is_approved":c.is_approved
        } for c in companies
    ], 200

def approve_company_controller(company_id):
    company = Company.query.get(company_id)
    if company:
        company.is_approved = True
        db.session.commit()
        return {"msg": "COMPANY APPROVED SUCCESSFULLY!"}, 200
    return abort(400)

def delete_company_controller(company_id):
    company = Company.query.get(company_id)
    if company:
        db.session.delete(company)
        db.session.commit()
        return {"msg": "COMPANY DELETED SUCCESSFULLY!"}, 200
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
            "date_of_birth":datetime.strftime(s.date_of_birth, "%d-%m-%Y"),
            "department":s.department,
            "cgpa":s.cgpa,
            "resume_url":s.resume_url,
            "is_placed":s.is_placed
        } for s in students
    ], 200

# is_active -> derived property
def get_placement_drives_controller():
    placement_drives=PlacementDrive.query.all()
    today=date.today()
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
            "start_date":datetime.strftime(p.start_date,"%d-%m-%Y"),
            "end_date":datetime.strftime(p.end_date,"%d-%m-%Y"),
            "is_approved":p.is_approved,
            "is_active": (p.start_date <= today) and (today <= p.end_date) and (p.is_approved)
        } for p in placement_drives
    ]

def toggle_placement_drive_status_controller(placement_drive_id):
    placement_drive=PlacementDrive.query.get(placement_drive_id)
    if placement_drive:
        placement_drive.is_approved=not(placement_drive.is_approved)
        db.session.commit()
        return {"msg": "PLACEMENT DRIVE APPROVED STATUS UPDATED SUCCESSFULLY!"}, 200
    return abort(400)

def get_applications_controller():
    applications = Application.query.all()
    return[
        {
            "id": a.id,
            "student_id": a.student_id,
            "placement_drive_id": a.placement_drive_id,
            "applied_date": datetime.strftime(a.applied_date, "%d-%m-%Y"),
            "application_status": a.application_status,
            "student_name": a.student.user.name,
            "student_email": a.student.user.email,
            "student_gender": a.student.gender,
            "student_date_of_birth": datetime.strftime(a.student.date_of_birth,"%d-%m-%Y").date(),
            "student_department": a.student.department,
            "student_cgpa": a.student.cgpa,
            "student_resume_url": a.student.resume_url,
            "student_is_placed": a.student.is_placed
        } for a in applications
    ], 200

def toggle_blacklist_controller(user_id):
    user=User.query.get(user_id)
    if user:
        user.is_blacklisted=not(user.is_blacklisted)
        db.session.commit()
        return {"msg": "BLACKLIST STATUS UPDATED SUCCESSFULLY!"}, 200
    return abort(400)