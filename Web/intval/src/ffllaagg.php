<?php
$ip = $_SERVER['REMOTE_ADDR'];
$str = md5($ip);
$flag2 = substr($str , 0 , 10);
$flag1 = "947eae96fe415cbc6eab17";

$flag = "0xGame{".$flag1.$flag2."}";
//0xGame{947eae96fe415cbc6eab17[a-f0-9]*}
//$flag='0xGame{e4zy_php_tricks}';