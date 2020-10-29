<?php
require_once 'class.php';
session_save_path('session');
ini_set('session.serialize_handler','php_serialize');
session_start();

if(isset($_POST['username'])&&isset($_POST['password'])){
    $user = new User($_POST['username'], $_POST['password'], $_POST['motto']);
    $user->register();
    echo 'register success!'."<br/>";
    echo '<a href="profile.php">click hear to see your motto</a>';
}else{
    die('empty username or password!');
}

?>