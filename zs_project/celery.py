# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 15:58
# @Author  : Alkad
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zs_project.settings')

app = Celery('zs_project'.encode('utf-8'))

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
