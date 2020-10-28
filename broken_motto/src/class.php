<?php
class User {
    public $username;
    public $password;
    public $motto;
    function __construct($username, $password, $motto)
    {
        $this->username = $username;
        $this->password = $password;
        $this->motto = $motto;
    }

    public function register(){
        $_SESSION['username'] = $this->username;
        $_SESSION['password'] = $this->password;
        $_SESSION['motto'] = $this->motto;
    }
}

class info{
    public $admin;
    public $username;
    public $motto;

    public function __construct()
    {
        $this->admin = 0;
        $this->motto = $_SESSION['motto'];
        $this->username = $_SESSION['username'];
    }

    public function __destruct()
    {
        echo 'your motto:'.$this->motto;
        if($this->admin===1){
            show_source('flag.php');
        }
    }
}