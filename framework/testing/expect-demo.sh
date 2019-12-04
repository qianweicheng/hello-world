#!/usr/bin/expect -f
# expect_out
spawn bash
expect "bash-3.2"
# send "echo exp_pid: $exp_pid\r"
# expect "%"
# send whoami\r
stty -echo
send_user "password: "
# expect_user -re "(.*)\n"
# expect_user -re "(a{1,})(.*)\n"
# send_user "\n"
# send "echo $expect_out(0,string)\r"
# send "echo $expect_out(1,string)\r"
send "echo $expect_out(buffer)\r"
stty echo
expect eof
exit
