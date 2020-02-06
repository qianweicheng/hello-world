C: ehlo weichengdembp.lan
S: 250-mail
S: 250-PIPELINING
S: 250-AUTH LOGIN PLAIN 
S: 250-AUTH=LOGIN PLAIN
S: 250-coremail 1Uxr2xKj7kG0xkI17xGrU7I0s8FY2U3Uj8Cz28x1UUUUU7Ic2I0Y2UFogpZ0UCa0xDrUUUUj
S: 250-STARTTLS
S: 250 8BITMIME
S: mail
S: PIPELINING
S: AUTH LOGIN PLAIN
S: AUTH=LOGIN PLAIN
S: coremail 1Uxr2xKj7kG0xkI17xGrU7I0s8FY2U3Uj8Cz28x1UUUUU7Ic2I0Y2UFogpZ0UCa0xDrUUUUj
S: STARTTLS
S: 8BITMIME
C: AUTH PLAIN AGVkb3Rlc3QyQDEyNi5jb20AQTEyMzQ1Njc=
S: 235 Authentication successful
S: Authentication successful
C: MAIL FROM:<edotest2@126.com>
S: 250 Mail OK
C: RCPT TO:<edisonshiln@126.com>
S: 250 Mail OK
C: DATA
S: 354 End data with <CR><LF>.<CR><LF>
C:
Content-Type: multipart/alternative;boundary="===============8533054211423644658=="
MIME-Version: 1.0
Subject: =?utf-8?q?x-amp-html_email_test?=
From: edotest2@126.com
To: edisonshiln@126.com

--===============8533054211423644658==
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64

dGhpcyBpcyBwbGFpbg==

--===============8533054211423644658==
Content-Type: text/x-amp-html; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64

PGRpdj50aGlzIGlzIHgtYW1wLWh0bWw8L2Rpdj4=

--===============8533054211423644658==
Content-Type: text/html; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: base64

PGRpdj50aGlzIGlzIGh0bWw8L2Rpdj4=

--===============8533054211423644658==--
.
S: 250 Mail OK queued as smtp7,DsmowACnrGxFFDlewRb+Aw--.25745S2 1580799046
S: Mail OK queued as smtp7,DsmowACnrGxFFDlewRb+Aw--.25745S2 1580799046
C: quit
S: 221 Bye
