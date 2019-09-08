<?php 

$fp=fopen("real.txt", "w+");
fwrite($fp, print_r($_POST, true));
fclose(fp);

$arr = array('text' => 'Use 603 218 to verify your Instagram account.');

$sms = json_encode($arr);
$sms_decode = json_decode($sms);
$sms_content = $sms_decode->{'text'};
//$security_code = str_replace('Use ', '', $sms_content);
//$security_code = str_replace(' to verify your Instagram account.', '', $security_code);
//$security_code = str_replace(' ', '', $security_code);
$security_code = $_GET['securitycode'];

echo $security_code;

$json_file = array('challenge' => array('security_code' => $security_code));

$fp2 = fopen("/home/ubuntu/InstaPy/logs/guillaumeteillet/securitycode.json", "w+");
fwrite($fp2, json_encode($json_file));
fclose($fp2);
?>