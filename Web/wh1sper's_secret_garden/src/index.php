<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>wh1sper's secret garden</title>
    <style type="text/css">
        body {background-image:url('background.jpg');}
        #card {
            background-color: rgba(248, 249, 247, 0.62);
            text-align: center;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            transition: 0.3s;
            width: 45%;
            border-radius: 5px;
            margin: auto;
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%,-50%);
        }

        #card:hover {
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.5);
        }
        #php {
            text-align: center;
            margin-bottom:25px;
        }

    </style>
</head>

<body>
<div id="card">

        <h1 id="h1">Welcome to wh1sper's secret garden</h1>
        <h4><br/></h4>
    <div id="php">
        <?php
        if(!preg_match('/wh1sper/i',$_SERVER['HTTP_USER_AGENT'])){
            die("你需要使用wh1sper浏览器来访问"."<br/>"."什么？没有？"."<br/>"."没有wh1sper浏览器还想打web？");
        }

        if(!preg_match('/ctf\.njupt\.edu\.cn/i',$_SERVER['HTTP_REFERER'])){
            die('你需要来自：https://ctf.njupt.edu.cn/');
        }

        if(!preg_match('/127\.0\.0\.1/i',$_SERVER['HTTP_X_FORWARDED_FOR'])){
            die('你得从本地访问才行哟！');
        }

        echo "呐~既然你这么厉害，flag就给你好了"."<br/>";
	echo "<img src='setu.jpg'></img><br/>";
        echo '0xGame{宁就是接头霸王?}';
        ?>
    </div>
</div>

</body>
</html>
