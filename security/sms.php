<?php 

$security_code = $_GET['securitycode'];

$fp2 = fopen("securitycode.json", "w+");
fwrite($fp2, $security_code);
fclose($fp2);
?>