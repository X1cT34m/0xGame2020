var current = null;
document.querySelector('#username').addEventListener('focus', function(e) {
  if (current) current.pause();
  current = anime({
    targets: 'path',
    strokeDashoffset: {
      value: 0,
      duration: 700,
      easing: 'easeOutQuart'
    },
    strokeDasharray: {
      value: '240 1386',
      duration: 700,
      easing: 'easeOutQuart'
    }
  });
});
document.querySelector('#password').addEventListener('focus', function(e) {
  if (current) current.pause();
  current = anime({
    targets: 'path',
    strokeDashoffset: {
      value: -336,
      duration: 700,
      easing: 'easeOutQuart'
    },
    strokeDasharray: {
      value: '240 1386',
      duration: 700,
      easing: 'easeOutQuart'
    }
  });
});
document.querySelector('#submit').addEventListener('focus', function(e) {
  if (current) current.pause();
  current = anime({
    targets: 'path',
    strokeDashoffset: {
      value: -730,
      duration: 700,
      easing: 'easeOutQuart'
    },
    strokeDasharray: {
      value: '530 1386',
      duration: 700,
      easing: 'easeOutQuart'
    }
  });
});

function doLogin(){
  var username = $("#username").val();
  var password = $("#password").val();
  if(username == "" || password == ""){
    $(".msg").text("用户名和密码不能为空!");
    return;
  }
  
  var data = "username="+username+"&"+"password="+password;
    $.ajax({
        type: "POST",
        url: "login.php",
        contentType: "application/x-www-form-urlencoded",
        data: data,
        anysc: false,
        success: function (result, status, xhr) {
          if(result == '成功'){
            window.location.href = 'admin.php';  
          }
          $(".msg").text(result);
          
        },
        error: function (XMLHttpRequest,textStatus,errorThrown) {
            $(".msg").text(errorThrown + ':' + textStatus);
        }
    }); 
}