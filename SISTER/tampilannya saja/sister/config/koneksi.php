<?php
    $server = "localhost";
    $username = "root";
    $password = "";
    $database = "sister";

    // Koneksi dan memilih database di server
    $con = mysqli_connect($server, $username, $password, $database) or die("Koneksi gagal");
    //mysql_select_db($database) or die("Database tidak bisa dibuka");

    function Con_Close($x){
      mysqli_close($x);
    }
?>
