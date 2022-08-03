#!/bin/sh

echo "init mysql"

python manage.py makemigrations
python manage.py migrate

echo "start scrapy data and write it to mysql"

cd ./spider/spider
scrapy crawl biglotto
scrapy crawl twocolorballs
#sed -i 's/limit=100000&sort=0/limit=10&sort=0/g' spiders/biglotto.py
#sed -i 's/limit=100000&sort=0/limit=10&sort=0/g' spiders/twocolorballs.py

cd ../../
python utils/mysql_utils.py


echo "start server"
#python manage.py runserver