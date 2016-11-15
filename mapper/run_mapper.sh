# @Author: Ritesh Pradhan
# @Date:   2016-07-18 14:22:01
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-08-25 00:08:36

mongodump --db mapper --archive=mapper.<date>.archive
mongorestore --db mapper --archive=/path/to/archive

#Run redis
./run-redis.sh

#Run Celery worker
celery -A mapper.celery  worker

sudo supervisorctl start mappercelery
sudo supervisorctl stop mappercelery
sudo supervisorctl start mappercelery
sudo supervisorctl status mappercelery

sudo supervisorctl restart  mappercelery
tail -f /var/log/celery/mapper_worker.log

(nohup python -u mapper.py &)




