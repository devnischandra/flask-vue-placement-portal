from flask import request, abort
from extensions import db, bcrypt
from models import User, Company, Student

from flask_jwt_extended import create_access_token

from datetime import datetime

def login_controller():
    data=request.get_json()
    email=data['email']
    password=data['password']

    if email and password:
        user=User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password_hash,password):
            current_user_id=user.id
            current_user_role=user.role
            additional_claims = {"current_user_role":str(user.role)}
            access_token=create_access_token(str(current_user_id),additional_claims=additional_claims)
            return {
                "msg":{
                    "current_user_role":current_user_role,
                    "token":access_token
                }
            },200
    return abort(400)

def company_registration_controller():
    data=request.get_json()
    name=data["name"]
    email=data["email"]
    password=data['password']
    hr_contact=data["hr_contact"] or None
    website_url=data["website_url"] or None

    existing_user=User.query.filter_by(email=email).first()

    if [name, email, password] and (not existing_user):
        password_hash=bcrypt.generate_password_hash(password).decode("utf-8")
        new_user=User(
            role="company",
            name=name,
            email=email,
            password_hash=password_hash
        )
        db.session.add(new_user)
        db.session.flush()

        new_company=Company(
            id=new_user.id,
            hr_contact=hr_contact,
            website_url=website_url
        )
        db.session.add(new_company)
        db.session.commit()
        return{
            "msg":"COMPANY REGISTERED SUCCESSFULLY!"
        },200
    return abort(400)

def student_registration_controller():
    data=request.get_json()
    name=data["name"]
    email=data["email"]
    password=data['password']
    gender=data["gender"]
    date_of_birth=data["date_of_birth"]
    department=data["department"]
    cgpa=data["cgpa"]
    resume_url=data["resume_url"] or None

    existing_user=User.query.filter_by(email=email).first()

    if [name, email, password] and (not existing_user):
        password_hash=bcrypt.generate_password_hash(password).decode("utf-8")
        new_user=User(
            name=name,
            email=email,
            password_hash=password_hash
        )
        db.session.add(new_user)
        db.session.flush()

        date_of_birth=datetime.strptime(date_of_birth,"%d-%m-%Y").date()

        new_student=Student(
            id=new_user.id,
            gender=gender,
            date_of_birth=date_of_birth,
            department=department,
            cgpa=cgpa,
            resume_url=resume_url
        )
        db.session.add(new_student)
        db.session.commit()
        return{
            "msg":"STUDENT REGISTERED SUCCESSFULLY!"
        },200
    return abort(400)