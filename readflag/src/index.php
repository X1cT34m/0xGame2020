<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta http-equiv="Content-type" content="text/html; charset=UTF-8">
    <style type="text/css">body {background-color: #FAFAFA;}.top-banner {background: #555;}input[type="text"] {-webkit-box-sizing: border-box;-moz-box-sizing: border-box;box-sizing: border-box;width: 100%;height: -webkit-calc(3em + 2px);height: calc(3em + 2px);margin: 0 0 1em;padding: 1em;border: 1px solid #cccccc;border-radius: 1.5em;background: #fff;resize: none;outline: none;}body {margin: 0;padding: 0;line-height: 1.5em;font-family: "Times New Roman", Times, serif;font-size: 20px;color: #000000;background: #5B6EB3 no-repeat;input[type="text"][required]:focus {border-color: #00bafa;}input[type="text"][required]:focus + label[placeholder]:before {color: #00bafa;}input[type="text"][required]:focus + label[placeholder]:before,input[type="text"][required]:valid + label[placeholder]:before {-webkit-transition-duration: .2s;transition-duration: .2s;-webkit-transform: translate(0, -1.5em) scale(0.9, 0.9);-ms-transform: translate(0, -1.5em) scale(0.9, 0.9);transform: translate(0, -1.5em) scale(0.9, 0.9);}input[type="text"][required]:invalid + label[placeholder][alt]:before {content: attr(alt);}input[type="text"][required] + label[placeholder] {display: block;pointer-events: none;line-height: 2.3em;margin-top: -webkit-calc(-3em - 2px);margin-top: calc(-3em - 2px);margin-bottom: -webkit-calc((3em - 1em) + 2px);margin-bottom: calc((3em - 1em) + 2px);}input[type="text"][required] + label[placeholder]:before {content: attr(placeholder);display: inline-block;margin: 0 -webkit-calc(1em + 2px);margin: 0 calc(1em + 2px);padding: 0 2px;color: #898989;white-space: nowrap;-webkit-transition: 0.3s ease-in-out;transition: 0.3s ease-in-out;background-image: -webkit-gradient(linear, left top, left bottom, from(#ffffff), to(#ffffff));background-image: -webkit-linear-gradient(top, #ffffff, #ffffff);background-image: linear-gradient(to bottom, #ffffff, #ffffff);-webkit-background-size: 100% 5px;background-size: 100% 5px;background-repeat: no-repeat;background-position: center;}</style>
</head>
<body>
    <div style="width:400px;height:10px;margin:100px auto">
        <form action="index.php" method="post"> 
            <input type="text" name="cmd" placeholder="请输入Linux命令">
        </form>
<?php
if(isset($_POST['cmd'])) {
@system($_POST['cmd']);
}
?>
        <!-- Where is flag? -->
        <!-- Oh! It's in / -->
    </div>
</body></html>