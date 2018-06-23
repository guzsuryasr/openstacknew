<?php
      session_start();
      session_destroy();
      echo "<script>alert('Anda telah keluar dari Halaman');
          window.location = 'index.html'</script>";
?>
