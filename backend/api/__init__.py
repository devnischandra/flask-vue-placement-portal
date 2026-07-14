from flask import Blueprint

from .routes.auth import auth_bp
from .routes.admin import admin_bp

api_bp = Blueprint("api", __name__, url_prefix="/api/v2")

api_bp.register_blueprint(auth_bp)
api_bp.register_blueprint(admin_bp)

