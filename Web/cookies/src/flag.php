<?php
$ip = $_SERVER['REMOTE_ADDR'];
$str = md5($ip);
$flag2 = substr($str , 0 , 10);
$flag1 = "b3c48a2f54bb49c60a0d08";

$flag = "0xGame{".$flag1.$flag2."}";