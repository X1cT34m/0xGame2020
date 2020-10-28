#!/bin/bash
sleep 5
/etc/init.d/apache2 start
/etc/init.d/mysql start
mysql -e "create user 'www-data' identified by '';"
mysql -e "create database user;"
mysql -e "create table user.user(id int,username char(20),password char(50));"
mysql -e "insert into user.user value(1,'admin','p@sswd_for_admin');"
mysql -e "insert into user.user value(2,'root','there_is_no_flag');"
mysql -e "insert into user.user value(3,'flag','flag{this_\!s_flag}');"
mysql -e "insert into user.user value(4,'wh1sper','0xGame{blind_sqli_1s_not_hard}');"
mysql -e "GRANT SELECT ON user.user TO 'www-data'@'%';"
mysql -e "flush privileges;"
rm /app/start.sh
