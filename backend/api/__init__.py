from flask import Blueprint

from .routes.auth import auth_bp
from .routes.admin import admin_bp
from .routes.company import company_bp
from .routes.student import student_bp

api_bp = Blueprint("api", __name__, url_prefix="/api/v2")

api_bp.register_blueprint(auth_bp)
api_bp.register_blueprint(admin_bp)
api_bp.register_blueprint(company_bp)
api_bp.register_blueprint(student_bp)