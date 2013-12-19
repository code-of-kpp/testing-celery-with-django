from __future__ import print_function

from celery import task


@task(name='hi')
def print_hello_task():
    print('Hello')
