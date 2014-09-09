//update message every second
function update_message(){
 var ip_input = document.getElementById('remote_ip').value;
 //var node_id = ipToid(ip_input);
 var remote_node_id = ipToid(ip_input)
 var req = new XMLHttpRequest();
 var d = new Date();
 var reqURL = '/cgi-bin/web_im/read_msg.sh?remote_node_id=' + remote_node_id + '&_=' + d.getTime();
 req.onreadystatechange = function(){
     if(req.readyState == 4){
         if(req.status == 200){
             var msg_div = document.getElementById('msg_div');
             var msgs = req.responseText;
             msg_div.innerHTML = msgs;
         }
     }
 }
	
 //var formData = new FormData();
 //formData.append('cmd', 'get_msg');
 //formData.append('remote_node_id', remote_node_id);
 req.open('GET', reqURL, true);
 req.send();
}
setInterval(update_message, 1000);

//send message to remote node
function send_message(){
 	var message = document.getElementById('message').value;
	var ip_input = document.getElementById('remote_ip').value;
	var req = new XMLHttpRequest(); 
	var d = new Date();
 	var reqURL = '/cgi-bin/web_im/chat_util.py?' + d.getTime();
 	var formData = new FormData();
 	formData.append('cmd', 'send_msg');
 	formData.append('msg', message);
	formData.append('remote_ip', ip_input);
 	req.onreadystatechange = function(){
     		if(req.readyState == 4){
         		if(req.status == 200){
             			var msgs = req.responseText;
             			console.log(msgs);
         		}
     		}
 	}

 	req.open('POST', reqURL, true);
 	req.send(formData);
}
/*
close server when leave im window
*/
$(window).bind('beforeunload', function() { 
     var req = new XMLHttpRequest(); 
     var d = new Date();
     var reqURL = '/cgi-bin/web_im/chat_util.py?' + d.getTime();
     var formData = new FormData();
     formData.append('cmd', 'close_chat');
     req.open('POST', reqURL, true);
     req.send(formData);
 })

/*
try connect to remote node
1 should show error message when unable to connect
2 show can connect message
*/
function connect_remote(){
	var ip_input = document.getElementById('remote_ip').value;
	var req = new XMLHttpRequest(); 
	var d = new Date();
     	var reqURL = '/cgi-bin/web_im/chat_util.py?' + d.getTime();
     	var formData = new FormData();
     	formData.append('cmd', 'connect_remote');
	formData.append('remote_ip', ip_input);
     	req.open('POST', reqURL, true);
     	req.send(formData);
}

//get node ip from node id
function idToIP(id) {
    var ip = '172.20.';
    var msb = Math.floor((parseInt(id)/256));
    var lsb = parseInt(id) - msb * 256;
    ip = ip + msb.toString() + '.' + lsb.toString();
    return ip;
}
//get node id from node ip
function ipToid(ip){
	var ip2 = ip.split('.')[2];
	var ip3 = ip.split('.')[3];
	var id = parseInt(ip2) * 256 + parseInt(ip3);
	return id;
}

/*
clear history with the node selected
*/
function clear_history(){
	var ip_input = document.getElementById('remote_ip').value;
	var req = new XMLHttpRequest(); 
	var d = new Date();
     	var reqURL = '/cgi-bin/web_im/chat_util.py?' + d.getTime();
     	var formData = new FormData();
	//var node_id = ipToid(ip_input)
	var remote_node_id = ipToid(ip_input);
     	formData.append('cmd', 'clear_history');
	formData.append('remote_node_id', remote_node_id);
     	req.open('POST', reqURL, true);
     	req.send(formData);
}

/*
clear all history
*/
function clear_all_history(){
	var req = new XMLHttpRequest(); 
	var d = new Date();
     	var reqURL = '/cgi-bin/web_im/chat_util.py?' + d.getTime();
     	var formData = new FormData();
	//var node_id = ipToid(ip_input)
	var remote_node_id = ipToid(ip_input);
     	formData.append('cmd', 'clear_all_history');
     	req.open('POST', reqURL, true);
     	req.send(formData);
}

/*
change nickname
*/
function change_nickname(){
	var name = prompt("Please enter your new nickname", "Me");
	if (name != null) {
		var req = new XMLHttpRequest(); 
		var d = new Date();
		var reqURL = '/cgi-bin/web_im/chat_util.py?' + d.getTime();
		var formData = new FormData();
		formData.append('cmd', 'change_nickname');
		formData.append('nickname', name);
		req.open('POST', reqURL, true);
		req.send(formData);
	}	
}

