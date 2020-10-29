<?php
error_reporting(0);//flag in flag.php
$id = $_POST['id']?$_POST['id']:0;
$file = $_POST['file']?$_POST['file']:"";

if($id == '2'){
	die("no no no !");
}
switch ($id) {
	case 0:
		die('<h1 align="center"><font color="red">Do you know vim in Linux?</font></h1>');
	case 1:
		die("0xGame Good!");
	case 2:
		if(preg_match('/filter|base64/', $file)){
           die("hacker");
        }
        include($file);
}