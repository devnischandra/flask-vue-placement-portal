from flask import Blueprint
from ..controllers.student import(
    get_me_controller,
    update_student_controller,
    get_companies_controller,
    get_placement_drives_controller,
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

# get me
@student_bp.route('/')
def get_me():
    return get_me_controller()
# update student
@student_bp.route('/', methods=['POST'])
def update_student():
    return update_student_controller()

# companies
@student_bp.route('/companies', methods=['GET'])
def get_companies():
    return get_companies_controller()

# placement_drives
@student_bp.route('/placement-drives', methods=['GET'])
def get_placement_drives():
    return get_placement_drives_controller()

# create application
@student_bp.route('/applications/', methods=['POST'])
def create_application():
    return create_application_controller()

# get applications
@student_bp.route('/applications', methods=['GET'])
def get_applications():
    return get_applications_controller()