from celery.task import task
import logging

logger = logging.getLogger("async_deploy_task")

@task
def a(x,y):
    return x+y