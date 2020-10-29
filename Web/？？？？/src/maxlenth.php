<?php
header("content-type:text/html;charset=utf-8");
$hint = "flag不在这，I prepared a shell for you : sh3ll.php";
$ip = $_POST['ip'];
if($ip === "yulige"){
    echo $hint;
}else{
    die("no right! input again");
}