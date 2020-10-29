<?php
header("Content-type: text/html; charset=utf-8");
include 'config.php';
//show_source(__FILE__);

if(!isset($_POST['username'])&&!isset($_POST['password']))
{
    die();
}

$username = $_POST['username'];
$password = $_POST['password'];

$con = @mysql_connect("localhost", $dbusername);

$select_db = mysql_select_db("$database");

if (!$select_db) {

    die("could not connect to the db:\n" .  mysql_error());

}

//查询代码

$sql = "select username from user where username='". $username ."' and password='". $password ."';";

//echo "你的查询语句是:  ".$sql."<br/>";

$res = mysql_query($sql);

if (@mysql_num_rows($res)<=0) {

    die("数据库里没你这号人,别想骗劳资.jpg");

}

echo "数据库有你这号人，那又怎么着？";

//查询代码

//关闭数据库连接

mysql_close($con);

?>
