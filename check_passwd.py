#!/usr/bin/env python3

'''
Short script checking pwnedpasswords.com for a
chosen password
'''

import requests
import hashlib

def h(string):
	''' returns sha1 of the password '''
	h = hashlib.sha1()
	h.update(string.encode())
	return h.hexdigest()

i = input('Enter password to check...\n')
hashed = h(i).upper()

url = 'https://api.pwnedpasswords.com/range/'
r = requests.get(url + hashed[:5])
n = r.text.find(hashed[5:]) #checks if hash is in the list

if n != -1:
	print('#'*20)
	print('FOUND MATCH!')
	print('#'*20)

	#creates key value pairs of the returned hashes
	lines = r.text.split('\n')
	pairs = {}
	for line in lines:
		kv = line.split(':')
		pairs[kv[0]] = kv[1].replace('\r', '')
	
	print('Hash: ', hashed)
	print('Matches: ', pairs[hashed[5:]])

else:
	print('Match not found')