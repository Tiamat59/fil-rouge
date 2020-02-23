import os
import time

user = "root"
password = "toor"
host = "fil-rouge_db_1"
database = "filrouge_db"
filestamp = time.strftime('%Y-%m-%d-%I:%M')
backup_name = database+"_"+filestamp

os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c > /root/mysql-backup/%s.gz" % (user,password,host,database,backup_name))
    