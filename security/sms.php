<?php 

$fp=fopen("real.txt", "w+");
fwrite($fp, print_r($_POST, true));
fclose(fp);

$arr = array('text' => 'Use 603 218 to verify your Instagram account.');

$sms = json_encode($arr);
$sms_decode = json_decode($sms);
$sms_content = $sms_decode->{'text'};
$security_code = str_replace('Use ', '', $sms_content);
$security_code = str_replace(' to verify your Instagram account.', '', $security_code);
$security_code = str_replace(' ', '', $security_code);

echo $security_code;

$fp2 = fopen("debug.txt", "w+");
fwrite($fp2, $security_code."\n");
fclose($fp2);
?>