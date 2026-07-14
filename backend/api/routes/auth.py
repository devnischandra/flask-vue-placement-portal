from flask import Blueprint
from api.controllers.auth import login_controller, company_registration_controller, student_registration_controller, me_controller

from flask_jwt_extended import jwt_required

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    return login_controller()

@auth_bp.route("/company-registration", methods=["POST"])
def company_registration():
    return company_registration_controller()

@auth_bp.route("/student-registration", methods=["POST"])
def student_registration():
    return student_registration_controller()