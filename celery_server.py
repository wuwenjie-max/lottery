from celery import Celery
import os
from celery.schedules import crontab

from lottery import settings


celery_app = Celery('celery server', broker=settings.BROKER_URL, config_source=settings)


@celery_app.task
def spider_data_to_db():
    os.system('cd {}/spider/spider && scrapy crawl biglottoday'.format(settings.BASE_DIR))
    os.system('cd {}/spider/spider && scrapy crawl twocolorballsday'.format(settings.BASE_DIR))
    os.system('python {}/utils/mysql_utils.py'.format(settings.BASE_DIR))

celery_app.conf.beat_schedule = {
    "day_task": {
        "task": "celery_server.spider_data_to_db",
        "schedule": crontab(hour='*/12'),
        "args": (),
    }
}


if __name__ == '__main__':
    # beat job: celery -A celery_server beat -l DEBUG -f logs/celery_beat.logs -D
    # exec job: celery -A celery_server worker -l DEBUG -c 1 -f logs/celery_worker.logs -D
    # celery_app.start()
    print('celery app init success')

