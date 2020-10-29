FROM php:7.2-apache

COPY ./src /var/www/html
COPY ./flag /flag
RUN chmod 444 /flag && chmod -R 755 /var/www/html
