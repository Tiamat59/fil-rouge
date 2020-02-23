FROM alpine

RUN apk update
RUN apk add mysql-client python3

WORKDIR /root/
ADD script/db-backup.py script/

CMD tail -f /dev/null
