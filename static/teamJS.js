$(".btn").click(function(){
	var attr = $(this).attr("data-li");

	$(".btn").removeClass("active");
	$(this).addClass("active");

	$(".item").hide();

	if(attr == "NFCWest"){
			$("." + attr).show();
	}
	else if(attr == "NFCSouth"){
			$("." + attr).show();
	}
	else if(attr == "NFCEast"){
			$("." + attr).show();
	}
	else if(attr == "NFCNorth"){
			$("." + attr).show();
	}
	else if(attr == "AFCWest"){
			$("." + attr).show();
	}
	else if(attr == "AFCSouth"){
			$("." + attr).show();
	}
	else if(attr == "AFCNorth"){
			$("." + attr).show();
	}
	else if(attr == "AFCEast"){
			$("." + attr).show();
	}
	else if(attr == "Offense"){
		$("." + attr).show();
}
else if(attr == "Defense"){
		$("." + attr).show();
}
	else{
			$(".item").show();
	}
});


function SFFunc() {
location.replace("SF.html")
};

function BEARFunc() {
location.replace("BUF.html")
};

function BENFunc() {
location.replace("CIN.html")
};

function denFunc() {
location.replace("DEN.html")
};
function bufFunc() {
location.replace("BUF.html")
};
function cleFunc() {
location.replace("CLE.html")
};
function tbFunc() {
location.replace("TB.html")
};
function ariFunc() {
location.replace("ARI.html")
};
function lacFunc() {
location.replace("LAC.html")
};
function kcFunc() {
location.replace("KC.html")
};
function ind() {
location.replace("IND.html")
};
function dal() {
location.replace("DAL.html")
};
function mia() {
location.replace("MIA.html")
};

function phi() {
location.replace("PHI.html")
};
function atl() {
location.replace("ATL.html")
};


function nyg() {
location.replace("NYG.html")
};
function jax() {
location.replace("JAX.html")
};
function nyj() {
location.replace("NYJ.html")
};
function det() {
location.replace("DET.html")
};

function gb() {
location.replace("GB.html")
};
function car() {
location.replace("CAR.html")
};
function NE() {
location.replace("NE.html")
};
function LV() {
location.replace("LV.html")
};
function HOU() {
location.replace("HOU.html")
};
function TEN() {
location.replace("TEN.html")
};
function PIT() {
location.replace("PIT.html")
};
function bal() {
location.replace("BAL.html")
};
function MIN() {
location.replace("MIN.html")
};
function SEA() {
location.replace("SEA.html")
};
function LAR() {
location.replace("LAR.html")
};

function NO() {
location.replace("NO.html")
};

function WAS() {
location.replace("WAS.html")
};

$(".btn").click(function(){
	var attr = $(this).attr("data-li");

	$(".btn").removeClass("active");
	$(this).addClass("active");

	$(".item").hide();
	
	if(attr == "Offense"){
		$("." + attr).show();
}
else if(attr == "Defense"){
		$("." + attr).show();
}
	else{
			$(".item").show();
		}
	});