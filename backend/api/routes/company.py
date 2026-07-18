from flask import Blueprint
from ..controllers.company import (
    create_placement_drive_controller,
    get_placement_drives_controller,
    update_placement_drive_controller,
    get_placement_drive_applications_controller,
    get_application_controller,
    update_application_controller
)

from flask_jwt_extended import jwt_required
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
    return get_placement_drives_controller()

# complete ongoing placement drive
@company_bp.route("/placement-drives/<int:placement_drive_id>", methods=['PATCH'])
def update_placement_drive(placement_drive_id):
    return update_placement_drive_controller(placement_drive_id)

# get placement drive -> applications
@company_bp.route("/placement-drives/<int:placement_drive_id>/applications", methods=['GET'])
def get_placement_drive_applications(placement_drive_id):
    return get_placement_drive_applications_controller(placement_drive_id)

# get application
@company_bp.route("/applications/<int:application_id>", methods=['GET'])
def get_application(application_id):
    return get_application_controller(application_id)

# update (status, interview_date, company_feedback)
@company_bp.route("/applications/<int:application_id>", methods=['PATCH'])
def update_application(application_id):
    return update_application_controller(application_id)


