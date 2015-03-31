
var notifications = WS4Redis({
    uri: 'ws://'+location.href.split("//")[1].split("/")[0]+'/ws/notifications?subscribe-user',
    heartbeat_msg: "--heartbeat--",
    receive_message: function(data){
    	var data = JSON.parse(data);
    	console.log(data);
    	$('.output').append("<div style='color:black'><b style='color:orange'>"+data.sender+"</b>:"+data.message+"</div>");
    }
});


$('#send_message').on('click', function(){
	$.ajax({'url':'/chat/message/?message='+$('#message').val()+"&username="+$('#username').val()}).success(function(data){
		console.log(data);
		$('#message').val("");
	})
});