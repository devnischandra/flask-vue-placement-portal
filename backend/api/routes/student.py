from flask import Blueprint
from ..controllers.student import(
    update_student_controller,
    get_companies_controller,
    get_company_placement_drives_controller,
    create_application_controller,
    get_applications_controller
)

from flask_jwt_extended import jwt_required
from ..guards import require_student

student_bp = Blueprint("student",__name__,url_prefix="/student")

@student_bp.before_request
@jwt_required()
def verify_student_role():
    require_student()

# update student
@student_bp.route('/students/<int:student_id>', methods=['POST'])
def update_student(student_id):
    return update_student_controller(student_id)

# get companies
@student_bp.route('/companies', methods=['GET'])
def get_companies():
    return get_companies_controller()

# get company -> placement_drives
@student_bp.route('/companies/<int:company_id>/placement-drives', methods=['GET'])
def get_company_placement_drives(company_id):
    return get_company_placement_drives_controller(company_id)

# create application
@student_bp.route('/placement-drives/<int:placement_drive_id>/applications', methods=['POST'])
def create_application(placement_drive_id):
    return create_application_controller(placement_drive_id)

# get applications
@student_bp.route('/applications', methods=['GET'])
def get_applications():
    return get_applications_controller()