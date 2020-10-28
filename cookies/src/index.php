<?php

	if(empty($_COOKIE["Cookie"])){
		setcookie("Cookie","eyJ1c2VybmFtZSI6Im51bGwiLCJzdGF0dXMiOjB9");
	}

	$ck = base64_decode($_COOKIE["Cookie"]);
	$json = json_decode($ck, true);
	$username=$json['username'];
	$status = $json['status'];
	$imgpath="./img/admin.jpg";
	if ($status == 0) {
		header("location:login.php");
	}
?>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>留言板</title>
	<link href="Css/bootstrap.css" rel="stylesheet" type="text/css" />
	<script type="text/javascript" src="Js/jquery.js"></script>
	<style type="text/css">
		.reply_btn{
			border:none;
			background:none;
			color:#337ab7;
		}
		.reply_btn:hover{
			border:none;
			cursor: pointer;
			text-decoration: underline;
			color: #ba1a09;
		}
	</style>
</head>
<body>
	<div align="right" style="padding:10px 50px;background:#00BFFF;">
		<h6 style="height:60px;line-height:60px;color:#fff;">欢迎&nbsp;&nbsp;<a><img src="<?php echo $imgpath; ?>" alt="头像" width="60" height="60" class="img-circle"/></a>&nbsp;&nbsp;<a href="index.php" style="color:#fff;"><?php echo $username; ?></a>&nbsp;登录留言板<span>&nbsp;&nbsp;&nbsp;<a href="action.php?a=quit" style="color:#fff;">退出登录</a></span></h6>
	</div>

	<br/>
		
	<h3 align="center">留言内容</h3>
	<div class="container" style="padding-left:150px;">
	<?php
	include("flag.php");
	$ck = base64_decode($_COOKIE["Cookie"]);
	$json = json_decode($ck, true);
	$username=$json['username'];
	$status = $json['status'];
	if($username === "admin" && $status == 1){
		echo "Y0u 4re admin, GiV3 u f14g : ".$flag;
	}else{
		echo "Y0u 4re n0t admin, no fl4g h3re!";
	}
	?>
	</div><br/>
	
</body>
</html>
