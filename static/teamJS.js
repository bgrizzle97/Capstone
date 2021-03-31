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
	else{
		$(".item").show();
	}
});

function myFunction() {
var popup = document.getElementById("myPopup");
popup.classList.toggle("show");
};