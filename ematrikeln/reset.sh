#! /bin/bash
echo "delete old db"
rm db.sqlite3
echo "run migrations"
python3 manage.py migrate
echo "apply fix"
python3 manage.py loaddata fixtures/dummyData.json fixtures/testData.json
echo "start new service"
screen -S ematrikeln python3 manage.py runserver orrwal.orriborri.com:8080
