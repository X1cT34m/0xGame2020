<?php
include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['0xGame']) && isset($_POST['X1cT34m'])){
	$a = $_GET['0xGame'];
	$b = $_POST['X1cT34m'];
	$c = 'acd666tql';
	if($a === $c && $b === $c){
		echo $flag;
	}
}else{
	die("Do you konw GET & POST ?");
}