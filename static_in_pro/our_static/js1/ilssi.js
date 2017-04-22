$(document).ready(function(){
	$(".flexslider").flexslider({
		animation: "slide"
	});
	
	$("#sitenav ul").superfish({
		animation: {height:'show'}
	});
	
	//Mobile Nav
	$("#sitenav-button").bind("click focus", function() {
		$("body").toggleClass("nav-menu");
		$("body").toggleClass("nav-button-expanded");                    
	});

	$("#sitenav").bind("testfit", function() {
		var width = window.innerWidth;

		$("body").removeClass("nav-menu");
		$("body").removeClass("nav-button");
		if ((width) && (width > 600)) {
			$("body").addClass("nav-menu");
			$("body").addClass("nav-button");
			$("body").removeClass("nav-button-expanded");
		}
	});

	$("#sitenav").trigger("testfit");
	
	//External links to open in new window
	$("a.external, a[href $='.pdf'], a[href $='.png'], a[href $='.jpg']").attr({target: "_blank"});
	
	//Old IE fixes
	$(".third:nth-child(3n+3), .quarter:nth-child(4n+4)").each(function(){
		$(this).addClass("last-split");
	});
});