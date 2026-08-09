from flask import Blueprint
from ..controllers.company import (
    create_placement_drive_controller,
    get_placement_drives_controller,
    update_placement_drive_controller,
    get_applications_controller,
    get_student_controller,
    update_application_controller,
    export_applications_controller
)

from flask_jwt_extended import jwt_required, get_jwt_identity
from ..guards import require_company

company_bp = Blueprint("company",__name__,url_prefix="/company")

@company_bp.before_request
@jwt_required()
def verify_company_role():
    require_company()

# create drive section
@company_bp.route("/placement-drives", methods=['POST'])
def create_placement_drive():
    return create_placement_drive_controller()

# get placement drives
@company_bp.route("/placement-drives", methods=['GET'])
def get_placement_drives():
    company_id = get_jwt_identity()
    return get_placement_drives_controller(int(company_id))

# mark as complete placement drive -> by updating end_date
@company_bp.route("/placement-drives/<int:placement_drive_id>", methods=['PATCH'])
def update_placement_drive(placement_drive_id):
    return update_placement_drive_controller(placement_drive_id)

# get -> applications
@company_bp.route("/applications", methods=['GET'])
def get_applications():
    company_id = get_jwt_identity()
    return get_applications_controller(int(company_id))

# get student
@company_bp.route("/students/<int:student_id>", methods=['GET'])
def get_student(student_id):
    return get_student_controller(student_id)

# update (status, interview_date, company_feedback)
@company_bp.route("/applications/<int:application_id>", methods=['PATCH'])
def update_application(application_id):
    return update_application_controller(application_id)

@company_bp.route("/export-applications", methods=["POST"])
def export_applications():
    return export_applications_controller()


