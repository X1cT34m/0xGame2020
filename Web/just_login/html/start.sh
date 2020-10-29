#!/bin/bash
/etc/init.d/apache2 start
/etc/init.d/mysql start
mysql -e "create user 'www-data' identified by '';"
mysql -e "create database user;"
mysql -e "create table user.user(id int,username char(20),password char(20));"
mysql -e "insert into user.user value(1,'admin','p@sswd_for_admin');"
mysql -e "GRANT SELECT ON user.user TO 'www-data'@'%';"
mysql -e "flush privileges;"
rm start.sh
