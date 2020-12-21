#!/usr/bin/python3
from binascii import crc32

target = 0x831721d9
chunck = [73, 72, 68, 82, 0, 0, 0, 0, 0, 0, 0, 0, 8, 6, 0, 0, 0]
for i in range(0xFFFF):
	for j in range(0xFFFF):
		chunck[6] = j >> 8
		chunck[7] = j % 256
		if crc32(bytes(chunck))==target:
			print("succeed!")
			print((hex(chunck[6]), hex(chunck[7]), hex(chunck[10]), hex(chunck[11])))
			exit()
	chunck[10] = i >> 8
	chunck[11] = i % 256
print("failed!")
