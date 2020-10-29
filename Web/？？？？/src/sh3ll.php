<?php
error_reporting(0);
highlight_file(__FILE__);
//echo "flag is in fl4g_is_here.php";

$cmd = $_POST['cmd'];
if(preg_match("/[A-Za-ko-z0-9]+/", $cmd)){
	die("hacker!");
}
$blacklist = "~!@#%^$&\/*()（）<>《》-_{}[]'/\":,";
        foreach(str_split($blacklist) as $char) {
            if(strchr($cmd, $char) !== false) 
                die('Big Hacker!!');
        }
system($cmd);
?>