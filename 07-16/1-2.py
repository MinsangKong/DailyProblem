# python3

import sys

con = "bkxznhdcwgpvjqtsrlmf"
vow = "aiyeou"
sen = sys.stdin.read().strip()
for i in sen:
	isup = False
	if ord(i) >= 65 and ord(i) <= 90:
		isup = True
		i = i.lower()
	if i in con:
		i = con[con.find(i)-10]
	elif i in vow:
		i = vow[vow.find(i)-3]
	if isup:
		i = i.upper()
	print(i,end="")