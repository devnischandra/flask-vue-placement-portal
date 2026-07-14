from flask import Blueprint
from ..controllers.admin import (
    search_controller,
    get_stats_controller,
    get_companies_controller,
    approve_company_controller,
    delete_company_controller,
    get_students_controller,
    get_placement_drives_controller,
    toggle_placement_drive_status_controller,
    get_applications_controller,
    toggle_blacklist_controller,
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

@admin_bp.route("/companies/<int:company_id>", methods=["PATCH"])
@jwt_required()
def approve_company(company_id):
    require_admin()
    return approve_company_controller(company_id)

@admin_bp.route("/companies/<int:company_id>", methods=["DELETE"])
@jwt_required()
def delete_company(company_id):
    require_admin()
    return delete_company_controller(company_id)

# student section
@admin_bp.route("/students")
@jwt_required()
def get_students():
    require_admin()
    return get_students_controller()

# placement drive section
@admin_bp.route("/placement-drives")
@jwt_required()
def get_placement_drives():
    require_admin()
    return get_placement_drives_controller()

@admin_bp.route("/placement-drives/<int:placement_drive_id>", methods=['PATCH'])
@jwt_required()
def toggle_placement_drive_status(placement_drive_id):
    require_admin()
    return toggle_placement_drive_status_controller(placement_drive_id)

# appication section
@admin_bp.route("/applications")
@jwt_required()
def get_applications():
    require_admin()
    return get_applications_controller()

# blacklist section
@admin_bp.route("/users/<int:user_id>", methods=["PATCH"])
@jwt_required()
def toggle_blacklist(user_id):
    require_admin()
    return toggle_blacklist_controller(user_id)







