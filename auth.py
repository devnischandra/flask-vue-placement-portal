from flask import request, abort
from extensions import db, bcrypt
from models import User, Company, Student

from flask_jwt_extended import create_access_token, get_jwt_identity
from datetime import datetime

def register_company_controller():
    request_data = request.get_json()

    # belongs to user model
    name = request_data.get("name")
    email = request_data.get("email")
    password = request_data.get("password")

    # belongs to company model
    # 'NONE' saves as 'NULL' in db
    hr_contact = request_data.get("hr_contact") or None
    website_url = request_data.get("website_url") or None
    
    existing_company = Company.query.join(User).filter(User.email==email).first()

    # 409: conflict
    if existing_company:
        return {"message": "COMPANY ALREADY EXISTS!"}, 409

    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    
    new_user = User(
        role="company",
        name=name,
        email=email,
        password_hash=password_hash
    )

    db.session.add(new_user)
    # saves it temporarily
    db.session.flush()

    new_company =  Company(
        id=new_user.id,
        hr_contact=hr_contact,
        website_url=website_url
    )

    db.session.add(new_company)
    db.session.commit()

    return {"message": "REGISTRATION SUCCESSFUL!"}, 201

def register_student_controller():
    request_data = request.get_json()

    # belongs to user model
    name = request_data.get("name")
    email = request_data.get("email")
    password = request_data.get("password")

    # belongs to student model
    gender = request_data.get("gender")
    # received as str
    date_of_birth_str = request_data.get("date_of_birth")
    department = request_data.get("department")
    cgpa = float(request_data.get("cgpa"))
    resume_url = request_data.get("resume_url") or None

    existing_user = User.query.filter_by(email=email).first()

    # 409: conflict
    if existing_user:
        return {"message": "STUDENT ALREADY EXISTS!"}, 409
    
    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    # str -> date obj
    date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d").date()
    
    new_user = User(
        name=name,
        email=email,
        password_hash=password_hash
    )

    db.session.add(new_user)
    db.session.flush()

    new_student = Student(
        id=new_user.id,
        gender=gender,
        date_of_birth=date_of_birth,
        department=department,
        cgpa=cgpa,
        resume_url=resume_url
    )

    db.session.add(new_student)
    db.session.commit()

    return {"message": "REGISTRATION SUCCESSFUL!"}, 201

def get_me_controller():
    current_user_id = int(get_jwt_identity())
    current_user = User.query.get(current_user_id)

    return {
        "current_user_id" : current_user.id,
        "current_user_name" : current_user.name
    }, 200