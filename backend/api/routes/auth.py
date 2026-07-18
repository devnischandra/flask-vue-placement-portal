from flask import Blueprint
from api.controllers.auth import (
    create_auth_token_controller,
    create_company_controller,
    create_student_controller
)

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/tokens", methods=["POST"])
def create_auth_token():
    return create_auth_token_controller()

@auth_bp.route("/companies", methods=["POST"])
def create_company():
    return create_company_controller()

@auth_bp.route("/students", methods=["POST"])
def create_student():
    return create_student_controller()