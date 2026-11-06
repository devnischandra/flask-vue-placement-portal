from flask import request, abort
from extensions import db, cache
from models import Company, PlacementDrive, Application, Student

from flask_jwt_extended import get_jwt_identity
from datetime import datetime, date, timedelta

from tasks.export_csv_tasks import company_applications

# create drive section
def create_placement_drive_controller():
    company_id = get_jwt_identity()
    company=Company.query.get(company_id)

    data=request.get_json()
    job_title=data.get("job_title")
    description=data.get("description")
    job_mode=data.get("job_mode")
    location=data.get("location") or None
    minimum_cgpa=data.get("minimum_cgpa")
    start_date=data.get("start_date")
    end_date=data.get("end_date")


    if company and job_title and description and job_mode and minimum_cgpa and start_date and end_date:
        new_placement_drive=PlacementDrive(
        company_id=company.id,
        job_title=job_title,
        description=description,
        job_mode=job_mode,
        location=location,
        minimum_cgpa=minimum_cgpa,
        start_date=datetime.strptime(start_date, "%Y-%m-%d").date(),
        end_date=datetime.strptime(end_date, "%Y-%m-%d").date()
        )

        db.session.add(new_placement_drive)
        db.session.commit()
        cache.delete_memoized(get_placement_drives_controller, int(company_id))
        return{"msg":"PLACEMENT DRIVE CREATED SUCCESSFULLY"}, 200
    return abort(400)
    



# get placement drives
@cache.memoize()
def get_placement_drives_controller(company_id):
    placement_drives=PlacementDrive.query.filter_by(company_id=company_id).all()
    return[
        {
            "id":p.id,
            "is_blacklisted": p.company.user.is_blacklisted,
            "job_title":p.job_title,
            "description":p.description,
            "job_mode":p.job_mode,
            "location":p.location,
            "minimum_cgpa":p.minimum_cgpa,
            "start_date":datetime.strftime(p.start_date, '%Y-%m-%d'),
            "end_date":datetime.strftime(p.end_date, '%Y-%m-%d')
        } for p in placement_drives
    ]

def update_placement_drive_controller(placement_drive_id):
    company_id = get_jwt_identity()
    placement_drive=PlacementDrive.query.filter(PlacementDrive.company_id==company_id, PlacementDrive.id==placement_drive_id).first()
    data=request.get_json()

    if placement_drive and "end_date" in data:
        today=date.today()
        placement_drive.end_date=today-timedelta(days=1)
        db.session.commit()
        cache.delete_memoized(get_placement_drives_controller, int(company_id))
        return {"msg": "PLACEMENT DRIVE UPDATED SUCCESSFULLY!"}, 200
    return abort(400)

def get_applications_controller(company_id):
    applications=Application.query.join(PlacementDrive).filter(PlacementDrive.company_id==company_id).all()
    return[
        {
            "id":a.id,
            "student_id":a.student_id,
            "placement_drive_id":a.placement_drive_id,
            "applied_date":datetime.strftime(a.applied_date, '%Y-%m-%d'),
            "status":a.status,
            "interview_date":datetime.strftime(a.interview_date, '%Y-%m-%d') if (a.interview_date) else False,
            "company_feedback":a.company_feedback,
        } for a in applications
    ], 200

def get_student_controller(student_id):
    student=Student.query.get(student_id)
    if student:
        return {
            "id":student.id,
            "name":student.user.name,
            "email":student.user.email,
            "gender":student.gender,
            "date_of_birth":datetime.strftime(student.date_of_birth, '%Y-%m-%d'),
            "department":student.department,
            "cgpa":student.cgpa,
            "resume_url":student.resume_url
        }
    return abort(400)
    

# update placement drive status
def update_application_controller(application_id):
    company_id = get_jwt_identity()
    application=Application.query.join(PlacementDrive).filter(PlacementDrive.company_id==company_id, Application.id==application_id).first()
    data=request.get_json(silent=True) or {}

    if application:
        updated = False
        if "status" in data:
            status = data.get("status")
            if status not in {"applied", "shortlisted", "selected", "rejected", "cancelled"}:
                return abort(400)
            application.status = status
            updated = True
        if 'interview_date' in data:
            interview_date = data.get('interview_date')
            try:
                application.interview_date = datetime.strptime(interview_date, '%Y-%m-%d').date()
            except (TypeError, ValueError):
                return abort(400)
            updated = True
        if 'company_feedback' in data:
            application.company_feedback=data.get('company_feedback')
            updated = True

        if not updated:
            return abort(400)

        db.session.commit()
        return{'msg': 'COMPANY FEEDBACK UPDATED SUCCESSFULLY'}, 200
    return abort(400)

def export_applications_controller():
    company_id = get_jwt_identity()
    task = company_applications.delay(company_id)

    return{
        'msg': 'EXPORT STARTED!',
        'id': task.id
    }, 202
