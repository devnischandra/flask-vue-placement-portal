from flask import Blueprint
from ..controllers.admin import (
    search_controller,
    get_stats_controller,
    get_companies_controller,
    approve_pending_company_controller,
    reject_pending_company_controller,
    get_students_controller,
    toggle_blacklist_controller,
    get_placement_drives_controller,
    complete_ongoing_placement_drive_controller,
    get_applications_controller,
    get_student_controller
)

from flask_jwt_extended import jwt_required
from ..guards import require_admin

admin_bp = Blueprint("admin",__name__,url_prefix="/admin")

# search section
@admin_bp.route("/search")
# jwt -> required token (authorization)
@jwt_required()
def search():
    require_admin()
    return search_controller()

# stats section
@admin_bp.route("/stats")
@jwt_required()
def get_stats():
    require_admin()
    return get_stats_controller()

# company section
@admin_bp.route("/companies")
@jwt_required()
def get_companies():
    require_admin()
    return get_companies_controller()

@admin_bp.route("/companies/<int:company_id>/approve-pending-company", methods=["PATCH"])
@jwt_required()
def approve_pending_company(company_id):
    require_admin()
    return approve_pending_company_controller(company_id)

@admin_bp.route("/companies/<int:company_id>/reject-pending-company", methods=["PATCH"])
@jwt_required()
def reject_pending_company(company_id):
    require_admin()
    return reject_pending_company_controller(company_id)

# student section
@admin_bp.route("/students")
@jwt_required()
def get_students():
    require_admin()
    return get_students_controller()

# blacklist section
@admin_bp.route("/users/<int:user_id>/toggle-blacklist", methods=["PATCH"])
@jwt_required()
def toggle_blacklist(user_id):
    require_admin()
    return toggle_blacklist_controller(user_id)

# placement drive section
@admin_bp.route("/placement-drives")
@jwt_required()
def get_placement_drives():
    require_admin()
    return get_placement_drives_controller()

@admin_bp.route("/placement-drives/<int:placement_drive_id>/complete-ongoing-placement-drive", methods=['PATCH'])
@jwt_required()
def complete_ongoing_placement_drive(placement_drive_id):
    require_admin()
    return complete_ongoing_placement_drive_controller(placement_drive_id)

# appication section
@admin_bp.route("/applications")
@jwt_required()
def get_applications():
    require_admin()
    return get_applications_controller()

@admin_bp.route("/students/<int:student_id>", methods=["GET"])
@jwt_required()
def get_student(student_id):
    require_admin()
    return get_student_controller(student_id)






