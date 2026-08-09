from flask import Blueprint
from api.controllers.common import celery_task_status_controller

common_bp = Blueprint('common',__name__, url_prefix='/common')

@common_bp.route("/celery-task-status/<task_id>")
def celery_task_status(task_id):
    return celery_task_status_controller(task_id)