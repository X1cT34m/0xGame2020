<?php
require_once 'class.php';
//ini_set('session.serialize_handler','php_serialize');
session_save_path('session');
session_start();

if(isset($_SESSION['username'])){
    $info = new info();
}else{
    die('出错啦！读取不到你的格言QWQ');
}
