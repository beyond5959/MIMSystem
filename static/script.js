$(function(){
	var headers=$("header");
	if (headers.length==0) 
		return false;
	var navs=$("header:first nav");
	if (navs.length==0) 
		return false;
	var links=$("header:first nav:first a");
	var linkurl;
	for(var i=0;i<links.length;i++){
		linkurl=links[i].getAttribute('href');
		if(window.location.href.indexOf(linkurl)!=-1){
			links[i].className="here";
		}
	}
	n=new Date();
	$('#year').attr("value",n.getFullYear());
	$('#month').attr("value",n.getMonth()+1);
	$('#day').attr("value",n.getDate());
	$("#date").attr("value",n.getFullYear()+'-'+(n.getMonth()+1)+'-'+n.getDate());
	$("#date2").attr("value",n.getFullYear()+'-'+(n.getMonth()+1)+'-'+n.getDate());
})