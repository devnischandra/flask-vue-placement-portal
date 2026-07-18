from flask import abort
from models import User
from flask_jwt_extended import get_jwt_identity

def require_admin():
    id=get_jwt_identity()
    user=User.query.get(id)

    if user.role != "admin":
        abort(403)

def require_company():
    id=get_jwt_identity()
    user=User.query.get(id)

    if user.role != "company" or user.is_blacklisted:
        abort(403)

def require_student():
    id=get_jwt_identity()
    user=User.query.get(id)

    if user.role != "student" or user.is_blacklisted:
        abort(403)
