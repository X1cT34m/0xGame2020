<?php
highlight_file(__FILE__);
include("ffllaagg.php");
//1st
if(isset ($_GET['0xGame']) && isset($_GET['id'])) {
    if($_GET['0xGame'] !== '20201001' && preg_match('/^20201001$/',$_GET['0xGame']))
       echo 'Good job!'.'<br>';
    else
       die('Think it over!');
//2st
    $id=intval($_GET['id']);
    if($_GET['id'] != 1024 && $id === 1024)
        echo 'Congratulations!'.'<br>'.$flag;
    else
        die('Work harder!');
}
