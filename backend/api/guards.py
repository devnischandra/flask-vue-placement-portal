from flask import abort
from flask_jwt_extended import get_jwt

def require_admin():
    claims = get_jwt()
    current_user_role = claims.get("current_user_role")
    if current_user_role != "admin":
        abort(403)

def require_company():
    claims = get_jwt()
    current_user_role = claims.get("current_user_role")
    if current_user_role != "company":
        abort(403)

def require_student():
    claims = get_jwt()
    current_user_role = claims.get("current_user_role")
    if current_user_role != "student":
        abort(403)
