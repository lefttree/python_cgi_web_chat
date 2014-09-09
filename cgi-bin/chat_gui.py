#!/usr/bin/python
import os

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Streamscape Web IM</title>'
print '<script language="javascript" type="text/javascript" src="../lib/jquery-1.7.2.min.js"></script>'
print "<script language='javascript' type='text/javascript' src='lib/web_chat.js'></script>"
print '<script language="javascript" type="text/javascript" src="../lib/spin.js"></script>'
print '</head>'
print "<body  onunload='unload()'>"
print '<h2>Streamscape Web IM</h2>'
print "<table>"
print "<tr>"
print "<td>Remote Node IP:</td>"
print "<td><input type='text' id='remote_ip'/></td>"
print "<td><button type='button' onclick='connect_remote()'>Connect</button></td>"
print "</tr>"
print "</table>"
print "<div id='msg_div' style='overflow:auto; width:65%; height:70%; border-style:outset; border-color:blue; border-radius:5px'></div>"  
print "<table style='width: 65%'>"
print "<tr>"            
print "<td style='width:80%'><input type='text' style='width:100%' id='message'/></td>"  
print "<td style='width:20%'><button type='button' style='width:100%' onclick='send_message()'>Send Message!</button></td>"
print "</tr></table><table><tr>"
print "<td><button type='button' onclick='change_nickname()'>Change Nickname</button></td>"
print "<td><button type='button' onclick='clear_history()'>Clear History</button></td>"
print "<td><button type='button' onclick='clear_all_history()'>Clear All History</button></td>"
print "</tr>"
print "</table>"
os.system('/usr/local/cgi-bin/web_im/chat_server.py &')
print '</body>'
print '</html>'

