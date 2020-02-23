FROM alpine

RUN apk update
RUN apk add apache2 git

WORKDIR var/www/localhost/
RUN rm -rf htdocs
RUN git clone https://github.com/Tiamat59/crossover.git htdocs

EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

