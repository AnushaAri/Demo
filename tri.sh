#!/usr/bin/expect -f
set PASS "Tel@12345"
#log_user 0                   # turn off the usual output
spawn ./tel.sh 
expect "login"
send  "root\r"
expect  "password"
send  "$PASS\r"
expect "Updated"
send "\n\r"

spawn ./question.sh
expect "Hello, How are you?\r"
send  "I am fine\r"
expect "password\r"
send  "$PASS\r"
expect "Can I ask you some questions?\r"
send -- "Sure\r"
expect "What is your favorite topic?\r"
send -- "Technology\r"

expect eof
