<?php
  include "config/koneksi.php";

  $username = $_POST['username'];
  $password = $_POST['password'];


  $login = mysqli_query($con, "SELECT * FROM login WHERE username='$username' AND password='$password'");

  //$ketemu = mysqli_num_rows($login);
  $r = mysqli_fetch_array($login, MYSQLI_ASSOC);

  //close connection
  Con_Close($con);
  // Apabila username dan password ditemukan
  if ($r == TRUE){
    session_start();

    $_SESSION['namauser'] = $r['username'];
    $_SESSION['passuser'] = $r['password'];
    $_SESSION['nama'] = $r['nama'];
    header('location:home.html');
  }
  else{
    
    echo "
      <div class='alert alert-danger' role='alert'>
        <center>LOGIN GAGAL! <br>
        Username atau Password Anda salah,<br>
        Atau account Anda sedang diblokir...<br>
        <a href=index.html><b>Ulangi kembali</b></a>
        </center>
      </div>";
  }
?>
