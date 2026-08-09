from celery_app import celery
from celery.result import AsyncResult

def celery_task_status_controller(task_id):
    task = AsyncResult(task_id, app=celery)
    
    if task.state == 'SUCCESS':
        return {
            'status': 'COMPLETED',
            'filename': task.result
        }, 200

    if task.state == 'PENDING':
        return {
            'status': 'PENDING',
        }, 200

    if task.state == 'FAILURE':
        return {
            'status': 'FAILED',
        }, 200

    return{
        'status': 'ERROR'
    }, 400
