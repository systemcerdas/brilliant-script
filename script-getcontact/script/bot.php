<?php
/**
* GetContact CLI Bot — versi bersih (tanpa access key marketing).
* Salinan asli dengan key gate: bot_original.php
* Author asli: Rusmana-ID / Inject-ID
*/

function clear_screen() {
	if (PHP_OS_FAMILY === 'Windows') {
		system('cls');
	} else {
		system('clear');
	}
}

function open_url($url) {
	$safe = escapeshellarg($url);
	if (PHP_OS_FAMILY === 'Windows') {
		pclose(popen('start "" ' . $safe, 'r'));
	} elseif (PHP_OS_FAMILY === 'Darwin') {
		exec('open ' . $safe);
	} else {
		exec('xdg-open ' . $safe);
	}
}

clear_screen();

$k = "\033[33;1m";
$h = "\033[32;1m";
$p = "\033[37;1m";
$m = "\033[31;1m";
$c = "\033[35;1m";
$o = "\033[30;1m";

echo $p."
██████╗ ███████╗████████╗ CONTACT
██╔════╝ ██╔════╝╚══██╔══╝
██║  ███╗█████╗     ██║
██║   ██║██╔══╝     ██║
╚██████╔╝███████╗   ██║
╚═════╝ ╚══════╝   ╚═╝   \n";

echo $p."╭────────────────────────────────╮\n";
echo $p."│   ".$h."Bot Cek Nomor Yang Di Save".$p."   │\n";
echo $p."│  ".$p."Author: Rusmana-ID   ".$p."         │\n";
echo $p."│         ".$p."Youtube: Inject-ID".$p."     │\n";
echo $p."╰────────────────────────────────╯\n";

echo $p."╭────────────────────────────────╮\n";
echo $p."│ ".$p."[".$h."01".$p."]".$k." Join Group Telegram       ".$p."│\n";
echo $p."│ ".$p."[".$h."02".$p."]".$k." Update Script             ".$p."│\n";
echo $p."│ ".$p."[".$h."03".$p."]".$k." Web Claim Crypto Free Unli".$p."│\n";
echo $p."│ ".$p."[".$h."04".$p."]".$h." Mulai Bot                 ".$p."│\n";
echo $p."│ ".$p."[".$h."05".$p."]".$h." Chat Admin                ".$p."│\n";
echo $p."│ ".$p."[".$h."06".$p."]".$c." Kumpulan Script           ".$p."│\n";
echo $p."│ ".$p."[".$m."00".$p."]".$m." Exit                      ".$p."│\n";
echo $p."╰────────────────────────────────╯\n";

$pil = readline($p."\n[".$h."•".$p."] Pilih No: ".$h);
if($pil == "1"){
	open_url("https://t.me/config_geratis");
	sleep(1);
	echo $p."[".$m."!".$p."] Run Lagi ketikan ".$k."php bot.php!\n\n";
	exit();
}elseif($pil == "2"){
	open_url("https://youtube.com/@Inject1D?feature=shared");
	sleep(1);
	echo $p."[".$m."!".$p."] Run Lagi ketikan ".$k."php bot.php!\n\n";
	exit();
}elseif($pil == "3"){
	open_url("https://tutorialinjectid.my.id");
	sleep(1);
	echo $p."[".$m."!".$p."] Run Lagi ketikan ".$k."php bot.php!\n\n";
	exit();
}elseif($pil == "5"){
	open_url("https://wa.me/6283879017166");
	sleep(1);
	echo $p."[".$m."!".$p."] Run Lagi ketikan ".$k."php bot.php!\n\n";
	exit();
}elseif($pil == "6"){
	open_url("https://t.me/config_geratis");
	sleep(1);
	echo $p."[".$m."!".$p."] Run Lagi ketikan ".$k."php bot.php!\n\n";
	exit();
}elseif($pil == "0"){
	echo $p."[".$m."!".$p."] Thanks You!\n\n";
	exit();
}elseif($pil == "4"){


	clear_screen();

	$k = "\033[33;1m";
	$h = "\033[32;1m";
	$p = "\033[37;1m";
	$m = "\033[31;1m";
	$c = "\033[35;1m";
	$o = "\033[30;1m";

	echo $p."
	██████╗ ███████╗████████╗ CONTACT
	██╔════╝ ██╔════╝╚══██╔══╝
	██║  ███╗█████╗     ██║
	██║   ██║██╔══╝     ██║
	╚██████╔╝███████╗   ██║
	╚═════╝ ╚══════╝   ╚═╝   \n";

	echo $p."╭────────────────────────────────╮\n";
	echo $p."│   ".$h."Bot Cek Nomor Yang Di Save".$p."   │\n";
	echo $p."│  ".$p."Author: Rusmana-ID   ".$p."         │\n";
	echo $p."│         ".$p."Youtube: Inject-ID".$p."     │\n";
	echo $p."╰────────────────────────────────╯\n";

echo $p."╭─────────────────────╮\n";
$no = trim(readline($p."│ ".$h."•".$p." Input No WhatsApp".$m." : ".$h));
echo $p."╰─────────────────────╯\n";

$ck = preg_match("/0/i",$no);
if($ck != "1"){
	echo $p."╭────────────────────────────────╮\n";
	echo $p."│  ".$m."Input No WhatsApp Dgn Benar!".$p."  │\n";
	echo $p."╰────────────────────────────────╯\n\n";
	exit();
}

//exit();
$chl = curl_init();
curl_setopt($chl, CURLOPT_URL, "https://getcontact.com/id/manage");
curl_setopt($chl, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($chl, CURLOPT_RETURNTRANSFER, 1);
$ua=array(
'sec-ch-ua-mobile: ?1',
'sec-ch-ua-platform: "Android"',
'upgrade-insecure-requests: 1',
'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'
);
curl_setopt($chl, CURLOPT_HTTPHEADER, $ua);
curl_setopt($chl, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($chl, CURLOPT_HEADER, 1);
$res = curl_exec($chl);
//echo $res;

$aks = explode("accessToken=",$res)[1];
$aks = explode(";",$aks)[0];
$tkn = explode('token=',$res)[1];
$tkn = explode('&',$tkn)[0];
$hash = explode('"hash":',$res)[1];
$hash = explode("'",$hash)[1];
$hash = explode("',",$hash)[0];
/*echo $aks."\n";
echo $tkn."\n";
echo $hash."\n";*/

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://widget.verifykit.com/v3.0/start");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
$ua=array(
'sec-ch-ua-platform: "Android"',
'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
'accept: application/json, text/plain, */*',
'sec-ch-ua: "Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
'content-type: application/json',
'sec-ch-ua-mobile: ?1',
'origin: https://gtc-manage-widget.verifykit.com',
'sec-fetch-site: same-site',
'sec-fetch-mode: cors',
'sec-fetch-dest: empty',
'referer: https://gtc-manage-widget.verifykit.com/'
);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
$data=('{"lang":"id","token":"'.$tkn.'","clientHost":"https://getcontact.com","validationType":"whatsapp","countryCode":"id","phoneNumber":"'.$no.'","deeplink":true}');
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
$res = curl_exec($ch);
$json = json_decode($res);
//print_r($json);

$ck = preg_match("/Anda memasukkan nomor telepon yang tidak sah/i",$res);
if($ck == "1"){
	echo $p."╭────────────────────────────────╮\n";
	echo $p."│  ".$m."Input No WhatsApp Dgn Benar!".$p."  │\n";
	echo $p."╰────────────────────────────────╯\n\n";
	exit();
}

echo $p."╭────────────────────────────────╮\n";
echo $p."│    ".$p."Silahkan Kirim Pesan Ini".$p."    │\n";
echo $p."│     ".$p."Melalui ".$c."WhatsApp".$p." Untuk".$p."     │\n";
echo $p."│      ".$p."Melakukan ".$k."Verifikasi".$p."      │\n";
echo $p."╰────────────────────────────────╯\n";

$wa = $json->result->validation->link;
$no = $json->result->phoneNumber->phoneNumber;

echo $p."╭────────────────────────────────╮\n";
echo $p."│ ".$h."Link WhatsApp Verifikasi:".$p." │\n";
echo $p."╰────────────────────────────────╯\n";
echo $c.$wa."\n\n";
open_url($wa);
echo $p."[".$h."•".$p."] Buka link di atas, kirim pesan WA, tunggu hitung mundur.\n\n";

echo $p."╭─────────────────────╮\n";
for ($i = 10; $i >= 0; $i--) {
	sleep(1);
	echo $p."\r│ ".$h."•".$p." Berakhir (".$k.$i.$p.") Detik! ";
}
echo $p."\n╰─────────────────────╯\n";


$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://widget.verifykit.com/v3.0/check");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
$ua=array(
'sec-ch-ua-platform: "Android"',
'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
'accept: application/json, text/plain, */*',
'sec-ch-ua: "Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
'content-type: application/json',
'sec-ch-ua-mobile: ?1',
'origin: https://gtc-manage-widget.verifykit.com',
'sec-fetch-site: same-site',
'sec-fetch-mode: cors',
'sec-fetch-dest: empty',
'referer: https://gtc-manage-widget.verifykit.com/'
);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
$data=('{"lang":"id","token":"'.$tkn.'","clientHost":"https://getcontact.com","phoneNumber":"'.$no.'","validationType":"whatsapp"}');
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
$res = curl_exec($ch);
$json = json_decode($res);
//print_r($json);

$suc = preg_match("/success/i",$res);
if($suc == "1"){
	$ses = $json->result->validation->sessionId;
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, "https://getcontact.com/validation-verifykit-check");
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_POST, 1);
	$ua=array(
	'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
	'referer: https://getcontact.com/id/manage',
	'cookie: lang=id',
	'cookie: cookieInform=accept',
	'cookie: accessToken='.$aks,
	'priority: u=1, i'

);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
$data=('hash='.$hash.'&sessionId='.$ses);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
$res = curl_exec($ch);
$json = json_decode($res);
///print_r($json);

$suc = preg_match("/success/i",$res);
if($suc == "1"){
	echo $p."╭────────────────────────────────╮\n";
	echo $p."│     ".$k."Verifikasi! ".$h."Berhasil!".$p."      │\n";
	echo $p."╰────────────────────────────────╯\n\n";

}
}else{
	echo $p."╭────────────────────────────────╮\n";
	echo $p."│      ".$k."Verifikasi! ".$m."Gagal!".$p."        │\n";
	echo $p."╰────────────────────────────────╯\n\n";
	exit();
}

$url = "https://getcontact.com/id/manage/profile";
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$ua=array(
'user-agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
'cookie: lang=id',
'cookie: _ga=GA1.1.1588411107.1733331413',
'cookie: cookieInform=accept',
'cookie: accessToken='.$aks
);
curl_setopt($ch, CURLOPT_HTTPHEADER, $ua);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
$res = curl_exec($ch);
$hsl = explode('<div class="pt-text">',$res);
$cek = count($hsl);
$krg = $cek -1;

echo $p."╭────────────────────────────────╮\n";
echo $p."│ ".$h."•".$k." Di ".$c."Save ".$k."Sebanyak ".$h.$krg.$p." Orang     \n";
echo $p."╰────────────────────────────────╯\n\n";

for ($l = 1; $l <= $krg; $l++) {
	$usr = explode('<div class="pt-text">',$res)[$l];
	$usr = explode('</div>',$usr)[0];
	echo $p."[".$h.$l.$p."]".$c." Di Save ".$k."-> ".$p.$usr."\n";
	sleep(1);
}
}


?>
