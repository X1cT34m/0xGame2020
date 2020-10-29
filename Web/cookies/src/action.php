<?php 
	header("content-type:text/html;charset=utf-8");

	$a=$_GET['a'];

	switch ($a) {
		case 'login':
			$uname = "admin";
			$passwd = "Leon@X1cT34m";
			if(isset($_POST['username']) && isset($_POST['userpass'])){
				$username=trim($_POST['username']);
				$userpass=md5($_POST['userpass']);
			}
			if($username === $uname && $userpass === md5($passwd)){
				setcookie("Cookie","eyJzdGF0dXMiOiIxIiwidXNlcm5hbWUiOiJhZG1pbiJ9");
			    die("<script>alert('登录成功');window.location.href='index.php';</script>");
			}elseif($username === $uname && $userpass !== md5($passwd)){
				die("<script>alert('admin密码有误，请重新登录');window.location.href='login.php';</script>");
			}else{
				$ck["username"] = $username;
				$ck["status"] = 1;
				$json = json_encode($ck, true);
				$b64 = base64_encode($json);
				setcookie("Cookie",$b64);
				die("<script>alert('登录成功');window.location.href='index.php';</script>");
			}

			break;

		case 'quit':
			setcookie("Cookie","eyJ1c2VybmFtZSI6Im51bGwiLCJzdGF0dXMiOjB9");
			header("location:login.php");

			break;
	}
