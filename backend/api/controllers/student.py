from flask import request, abort
from extensions import db
from models import User, Company, Student, PlacementDrive, Application

from flask_jwt_extended import get_jwt_identity
from datetime import datetime, date

def update_student_controller():
    student_id=get_jwt_identity()
    student=Student.query.join(User).filter(User.id==student_id).first()
    data=request.get_json()

    if student:
        if 'email' in data:
            email= data.get('email')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return {'msg': 'EMAIL ALREADY IN USE!'}, 409
            else:
                student.user.email = email
                db.session.commit()
                return {'msg': 'EMAIL UPDATED SUCCESSFULLY!'}, 200
        
        if 'cgpa' in data:
            student.cgpa = data.get('cgpa')
            db.session.commit()
            return {'msg': 'CGPA UPDATED SUCCESSFULLY!'}
        
        if 'resume_url' in data:
            student.resume_url = data.get('resume_url')
            db.session.commit()
            return {'msg': 'RESUME UPDATED SUCCESSFULLY!'}
    return abort(400)
        
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

def get_company_placement_drives_controller(company_id):
    placement_drives = PlacementDrive.query.filter_by(company_id=company_id).all()
    return [
        {
            "id":p.id,
            "job_title":p.job_title,
            "description":p.description,
            "job_mode":p.job_mode,
            "location":p.location,
            "minimum_cgpa":p.minimum_cgpa,
            "start_date":datetime.strftime(p.start_date,"%Y-%m-%d"),
            "end_date":datetime.strftime(p.end_date,"%Y-%m-%d")
        } for p in placement_drives
    ], 200

def create_application_controller(placement_drive_id):
    student_id=get_jwt_identity()
    student=Student.query.get(student_id)
    placement_drive=PlacementDrive.query.get(placement_drive_id)

    if student and float(student.cgpa) >= placement_drive.minimum_cgpa:
        new_application=Application(
            student_id=student_id,
            placement_drive_id=placement_drive_id,
            applied_date=date.today()
        )
        db.session.add(new_application)
        db.session.commit()

        return {'msg': "APPLICATION SUBMITTED SUCCESSFULLY!" }, 200
    return abort(400)

def get_applications_controller():
    student_id=get_jwt_identity()
    applications=Application.query.filter_by(student_id=student_id).all()
    return[
        {
            "id": a.id,
            "company_name": a.placement_drive.company.user.name,
            "job_title": a.placement_drive.job_title,
            "applied_date": datetime.strftime(a.applied_date, "%Y-%m-%d"),
            "status": a.status,
            "interview_date": datetime.strftime(a.interview_date, "%Y-%m-%d") if (a.interview_date) else None,
            "company_feedback": a.company_feedback,
        } for a in applications
    ], 200