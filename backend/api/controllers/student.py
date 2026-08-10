from flask import request, abort
from extensions import db
from models import User, Company, Student, PlacementDrive, Application

from flask_jwt_extended import get_jwt_identity
from datetime import datetime, date

from tasks.export_csv_tasks import student_applications

def get_me_controller():
    student_id=get_jwt_identity()
    student=Student.query.get(student_id)
    if student:
        return{
            "name":student.user.name,
            "email":student.user.email,
            "cgpa":student.cgpa,
            "resume_url":student.resume_url
        }
    return abort(400)

def update_student_controller():
    student_id=get_jwt_identity()
    student=Student.query.get(student_id)
    data=request.get_json()

    if student:
        if 'email' in data:
            email= data.get('email')
            existing_user = User.query.filter(
                User.id != student_id,
                User.email == email
            ).first()
            if existing_user:
                return {'msg': 'EMAIL ALREADY IN USE!'}, 409
            else:
                student.user.email = email
                db.session.commit()
        
        if 'cgpa' in data:
            student.cgpa = data.get('cgpa')
            db.session.commit()
        
        if 'resume_url' in data:
            student.resume_url = data.get('resume_url')
            db.session.commit()
        return {'msg': 'STUDENT PROFILE UPDATED SUCCESSFULLY!'}
    return abort(400)
        
def get_companies_controller():
    companies = Company.query.join(User).filter(User.is_blacklisted==False,Company.status=="approved").all()
    return [
        {
            "id":c.user.id,
            "name":c.user.name,
            "email":c.user.email,
            "hr_contact":c.hr_contact,
            "website_url":c.website_url
        } for c in companies
    ], 200

def get_placement_drives_controller():
    student_id = get_jwt_identity()

    placement_drives = (
        PlacementDrive.query
        .join(Company, PlacementDrive.company_id == Company.id)
        .join(User)
        .filter(
            User.is_blacklisted == False,
            Company.status == "approved"
        ).all()
    )

    return [
        {
            "id":p.id,
            "company_id": p.company.id,
            "company_name": p.company.user.name,
            "job_title":p.job_title,
            "description":p.description,
            "job_mode":p.job_mode,
            "location":p.location,
            "minimum_cgpa":p.minimum_cgpa,
            "start_date":datetime.strftime(p.start_date,"%Y-%m-%d"),
            "end_date":datetime.strftime(p.end_date,"%Y-%m-%d"),
            "has_applied": any(
                a.student_id == int(student_id)
                for a in p.applications
            )
        } for p in placement_drives
    ], 200

def create_application_controller():
    student_id=get_jwt_identity()
    student=Student.query.get(student_id)
    
    data=request.get_json()
    placement_drive_id=data.get("placement_drive_id")
    placement_drive=PlacementDrive.query.get(placement_drive_id)

    if not student or not placement_drive:
        return abort(400)

    today = date.today()
    is_active = today >= placement_drive.start_date and today <= placement_drive.end_date
    existing_application = Application.query.filter_by(placement_drive_id=placement_drive_id,student_id=student_id).first()

    if is_active and not existing_application:
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
            "placement_drive_id": a.placement_drive_id,
            "company_name": a.placement_drive.company.user.name,
            "job_title": a.placement_drive.job_title,
            "applied_date": datetime.strftime(a.applied_date, "%Y-%m-%d"),
            "placement_drive_start_date":datetime.strftime(a.placement_drive.start_date, "%Y-%m-%d"),
            "placement_drive_end_date": datetime.strftime(a.placement_drive.end_date, "%Y-%m-%d"),
            "status": a.status,
            "interview_date": datetime.strftime(a.interview_date, "%Y-%m-%d") if (a.interview_date) else None,
            "company_feedback": a.company_feedback,
        } for a in applications
    ], 200

def export_applications_controller():
    student_id = get_jwt_identity()
    task = student_applications.delay(student_id)

    return{
        'msg': 'EXPORT STARTED!',
        'id': task.id
    }, 202