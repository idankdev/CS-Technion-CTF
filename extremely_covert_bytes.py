#!/usr/bin/python3
from pwn import *

r = remote("ctf.cs.technion.ac.il", 4013)

flag = ''
found = ''

r.recv()
r.recv()
while found != '}':
	sendme = 'A'*(31-len(flag))
	r.sendline(sendme.encode())
	matchme = r.recvline().decode()[0:64]
	for i in range(33, 127):
		r.recv()
		r.sendline((sendme + flag + chr(i)).encode())
		response = r.recvline().decode()[0:64]
		if response == matchme:
			flag += chr(i)
			found = chr(i)
			break
	print(f"flag: {flag}")
	r.recv()	