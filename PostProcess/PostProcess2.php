<?php
echo 'Home: PostProcess';
echo "<br>";


if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        // get contents
   //$post_request_data = file_get_contents('php://input');
  // var_dump( $post_request_data);
$data = json_decode(file_get_contents('php://input'), TRUE);

extract($data);

if 	($src == "User" && $Name == "Step1-setup"){

	        	//$shipments = json_decode(file_get_contents("../Database/user.json"), true);
				//$shipments[] = $data;

				$data1 = json_encode($data);
				file_put_contents('../Database/SetUp.json', $data1."\n", FILE_APPEND );
				exec("../codes/SetUp.py '$sessionID' ");


}

elseif($src == "User" && $Name == "Step2-setup"){

				$data1 = json_encode($data);
				file_put_contents('../Database/SetUp.json', $data1."\n", FILE_APPEND );



}

elseif ($src == "User" && $Name == "Reconstruction1") {


				//$shipments = json_decode(file_get_contents("../Database/user.json"), true);
				//$shipments[] = $data;

				$data1 = json_encode($data);
				file_put_contents('../Database/Recon.json', $data1."\n", FILE_APPEND );
				exec("../codes/Nonces.py '$phaseID' ");
			}



elseif ($src == "User" && $Name == "Reconstruction2") {

				

				//$shipments = json_decode(file_get_contents("../Database/user.json"), true);
				//$shipments[] = $data;

				$data1 = json_encode($data);
				file_put_contents('../Database/Recon.json', $data1."\n", FILE_APPEND );
				exec("../codes/DistVeri.py '$phaseID' '$OnlineServers[0]' '$OnlineServers[1]'");
			}



elseif (($src == "CloudServer1" || $src == "CloudServer2") && $Name == "Step1-setup") {

	    	//$shipments = json_decode(file_get_contents("../Database/cloud1.json"), true);
				//$shipments[] = $data;

				$data1 = json_encode($data);
				file_put_contents('../Database/SetUp.json', $data1."\n", FILE_APPEND );
	    	}	

else {

				$data1 = json_encode($data);
				file_put_contents('../Database/Recon.json', $data1."\n", FILE_APPEND );


}

};

?>

