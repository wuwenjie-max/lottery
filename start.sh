#!/bin/sh

echo "shell useful by macos or centos"


echo "init mysql"
python manage.py makemigrations
python manage.py migrate
echo "init mysql ready"


if [ -f history_lock ]; then
  echo "history data was exists"
else
  echo "start scrapy history data and write it to mysql"
  cd ./spider/spider
  scrapy crawl biglotto
  scrapy crawl twocolorballs
  cd ../../
  python utils/mysql_utils.py
  echo "init history data ready"
  touch history_lock
fi


echo "start celery crontab job"
if [ -f celery_beat_pid ]; then
  cat celery_beat_pid |xargs kill -9
  rm -f celery_beat_pid
fi

if [ -f celery_worker_pid ]; then
  cat celery_worker_pid |xargs kill -9
  rm -f celery_worker_pid
fi

celery -A celery_server worker -l DEBUG -f logs/celery_worker.log -D --pidfile celery_worker_pid
celery -A celery_server beat -l DEBUG -f logs/celery_beat.log --detach --pidfile celery_beat_pid
echo "celery crontab job ready"


echo "start django server"
#python manage.py runserver
