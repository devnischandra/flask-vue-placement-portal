from flask import request, abort
from extensions import db, bcrypt
from models import User, Company, Student

from flask_jwt_extended import create_access_token

from datetime import datetime

def create_auth_token_controller():
    data=request.get_json()
    email=data.get('email')
    password=data.get('password')

    if email and password:
        user=User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password_hash,password) and (not user.is_blacklisted):
            current_user_role=user.role

            if current_user_role=="company":
                if (user.company.status=="pending"):
                    return {"msg":"WAIT FOR ADMIN APPROVAL!"}, 403
                if (user.company.status=="rejected"):
                    return {"msg":"YOUR REQUEST HAS BEEN REJECTED!"}, 403
            
            current_user_id=user.id
            access_token=create_access_token(str(current_user_id))
            return {
                    "current_user_role":user.role,
                    "token":access_token
            },200
    return abort(400)

def create_company_controller():
    data=request.get_json()
    name=data.get("name")
    email=data.get("email")
    password=data.get('password')
    hr_contact=data.get("hr_contact") or None
    website_url=data.get("website_url") or None

    existing_user=User.query.filter_by(email=email).first()

    if name and email and password and (not existing_user):
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

def create_student_controller():
    data=request.get_json()
    name=data.get("name")
    email=data.get("email")
    password=data.get('password')
    gender=data.get("gender")
    date_of_birth=data.get("date_of_birth")
    department=data.get("department")
    cgpa=data.get("cgpa")
    resume_url=data.get("resume_url") or None

    existing_user=User.query.filter_by(email=email).first()

    if name and email and password and (not existing_user):
        password_hash=bcrypt.generate_password_hash(password).decode("utf-8")
        new_user=User(
            name=name,
            email=email,
            password_hash=password_hash
        )
        db.session.add(new_user)
        db.session.flush()

        if gender and date_of_birth and department and cgpa:
            date_of_birth=datetime.strptime(date_of_birth,"%Y-%m-%d").date()
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