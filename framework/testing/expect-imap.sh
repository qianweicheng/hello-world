#!/usr/bin/expect -f
set timeout 5
set username edotest1 
set pwd *******
set host imap.126.com
set port 993
spawn openssl s_client -connect $host:$port -crlf
expect "* OK"
send "1 ID (\"name\" \"Edison\")\n"
expect "1 OK"
send "2 LOGIN $username $pwd\n"
expect {
    "2 OK" {}
    "2 NO" {    
        send_user "login failed.\n"
        exit    
    }
    timeout { 
        send_user "connection to IMAP server timed out\n"
        exit  
    }
}
send "3 SELECT INBOX\n"
expect "3 OK"
send "4 FETCH 1:2 UID\n"
expect "4 OK"
send "4 FETCH 2:3 BODYSTRUCTURE\n"
expect "4 OK"
send_user "Begin your own command here:\n"
interact