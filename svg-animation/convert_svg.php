<?php
	$debug=false;

	// send out the http and the svg header
	header("Content-Type: image/svg+xml;charset=utf8");
	print '<?xml version="1.0" standalone="no"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">';
	print '<svg width="100%" height="100%" version="1.1" xmlns="http://www.w3.org/2000/svg">';

	// data.php holds the map data for us
	require_once("data.php");
	//helper function used to print an array just in debug mode
	function printArray($array){
		global $debug;
		if($debug){
			echo "<pre>";
			print_r($array);
			echo "</pre>";
		}
	}
	
	//we parse the input in order to determine the transformation points
	$pontok=Array();
	foreach ($_GET as $key => $value){
		if(preg_match("/^x(\d*)$/", $key, $matches)==1){
			$num=$matches[1];
				if(isset($_GET["y".$num])){
					$pontok[]=Array($_GET["x".$num],$_GET["y".$num]);
				}
			}
	}
	printArray($pontok);
	function transformByOne($transformer,$pont){
		/*var d=Math.sqrt((pont[0]-mihez[0])*(pont[0]-mihez[0])+(pont[1]-mihez[1])*(pont[1]-mihez[1]));
            //bujatt's transformation
            var dmax=5000*mihez[3]/100;
            var dpi=Math.PI*d/2/dmax;
            var f=0;
            if(d<dmax){
				    f=Math.cos(dpi)*Math.cos(dpi)*Math.cos(dpi)*mihez[4]/100;
            }
            //end of bujatt's transformation
            pont[0]=pont[0]+f*(pont[0]-mihez[0]);
            pont[1]=pont[1]+f*(pont[1]-mihez[1]);
            return pont;*/
			   $d = hypot($pont[0]-$transformer[0],$pont[1]-$transformer[1]);
               $dmax = 255000;
               $pi = 3.1415926535898;
               $dpi = $d/2/$dmax*$pi;
               $f = 0;
        if($d<$dmax){
                       $f=cos($dpi)*cos($dpi)*cos($dpi)*15;
		//	$f=rand(0, 100)/100;
/*		} else {
			   $d = -$dmax+$d;
               $dpi = $pi*$d/2/$dmax;
                       $f=cos($dpi)*cos($dpi)*cos($dpi)*15;		
*/                       
		}
		return Array($pont[0]+$f*($pont[0]-$transformer[0]),
							$pont[1]+$f*($pont[1]-$transformer[1])) ;
	}
	function transform($pont){
		global $pontok;
		$epsilon=0.0005; // scale value
		foreach($pontok as $tpont){
			$pont=transformByOne($tpont,$pont);
		}
		return Array($pont[0]*$epsilon+600,$pont[1]*$epsilon+480);
	}
	function pont2string($pont){
		$pont=transform($pont);
		return $pont[0]." ".$pont[1]." ";
	}

	//helper function used to print out a path in svg format 
	function printPath($array,$stroke="black",$fill="none",$strokeOpacity=1,$fillOpacity=1){
		//move the pen to the first point
		echo "M".pont2string($array[0])." ";
		//draw all the points
		for ($i = 1; $i < count($array); $i++) {
			echo "L".pont2string($array[$i])." ";
		}
		//close the path
		echo "L".pont2string($array[0])." ";
	}
	//helper function used to print multiple paths
	function printPaths($paths,$stroke="black",$fill="none",$strokeOpacity=1,$fillOpacity=1){
		echo '<path stroke="'.$stroke.'" fill="'.$fill.'" stroke-opacity="'.$strokeOpacity.'" fill-opacity="'.$fillOpacity.'" d="';
		foreach($paths as $path){
			printPath($path,$stroke,$fill,$strokeOpacity,$fillOpacity);
		}
		echo '" />';
	}
	// colors: strokeColor, fillColor, strokeAlpha, fillAlpha
//	printPaths($korvonal,"rgb(255,0,0)","rgb(0,0,255)",0.9,1); 
//	printPaths($foutak,"black","rgb(0,0,255)",0,.5);
	printPaths($hidak,"black","black",0,1);
	printPaths($utcak,"black","black",0,1);
	
	//close the svg
	print "</svg>";
	
//this is the end of file