FROM alpine

RUN apk update
RUN apk add apache2 git

WORKDIR /etc/apache2/
RUN git -C /var/www/localhost/htdocs clone https://github.com/Tiamat59/crossover.git


EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

