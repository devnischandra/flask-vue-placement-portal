from flask import Blueprint
from ..controllers.admin import (
    search_controller,
    get_stats_controller,
    get_companies_controller,
    update_company_controller,
    get_students_controller,
    update_user_controller,
    get_placement_drives_controller,
    update_placement_drive_controller,
    get_applications_controller,
    get_student_controller
)

from flask_jwt_extended import jwt_required
from ..guards import require_admin

admin_bp = Blueprint("admin",__name__,url_prefix="/admin")

# jwt -> required token (authorization)
@admin_bp.before_request
@jwt_required()
def verify_admin_role():
    require_admin()

# do search
@admin_bp.route("/search")
def search():
    return search_controller()

# get stats
@admin_bp.route("/stats")
def get_stats():
    return get_stats_controller()

# get companies
@admin_bp.route("/companies")
def get_companies():
    return get_companies_controller()

# update company (status -> approve, reject)
@admin_bp.route("/companies/<int:company_id>", methods=["PATCH"])
def update_company(company_id):
    return update_company_controller(company_id)

# get students
@admin_bp.route("/students")
def get_students():
    return get_students_controller()

# update -> user blacklist status
@admin_bp.route("/users/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    return update_user_controller(user_id)

# get placement drives
@admin_bp.route("/placement-drives")
def get_placement_drives():
    return get_placement_drives_controller()

# complete ongoing placement drive
@admin_bp.route("/placement-drives/<int:placement_drive_id>", methods=['PATCH'])
def update_placement_drive(placement_drive_id):
    return update_placement_drive_controller(placement_drive_id)

# get applications
@admin_bp.route("/applications")
def get_applications():
    return get_applications_controller()

# get student
@admin_bp.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    return get_student_controller(student_id)






