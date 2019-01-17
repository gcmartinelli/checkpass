#!/usr/bin/env python3

'''
Short script checking pwnedpasswords.com for a
chosen password 

http://github.com/gcmartinelli/checkpass

Jan-2019
'''
import sys
import requests
import hashlib
import argparse

def h(string):
	''' returns sha1 of the password '''
	h = hashlib.sha1()
	h.update(string.encode())
	return h.hexdigest()

def check_pass(passw):
	hashed = h(passw).upper()
	#check API
	url = 'https://api.pwnedpasswords.com/range/'
	try:
		r = requests.get(url + hashed[:5])
	except Exception as e:
		print('Error contacting pwnedpasswords.com')
		print(e)
		sys.exit()
	n = r.text.find(hashed[5:]) #checks if hash is in the list

	if n != -1:
		#creates key value pairs of the returned hashes
		lines = r.text.split('\n')
		pairs = {}
		for line in lines:
			kv = line.split(':')
			pairs[kv[0]] = kv[1].replace('\r', '')	
		return [hashed, pairs[hashed[5:]]]
	else:
		return None

def main():
	parser = argparse.ArgumentParser(description="Checks pwnedpasswords.com for pwned passwords")
	parser.add_argument("source", help="filename or password to check")
	parser.add_argument("-f", "--filename", help="use an optional .txt sourcefile. One password per line", 
						action="store_true")
	parser.add_argument("-v", "--verbosity", help="increase verbosity", 
						action="store_true")
	args = parser.parse_args()

	if args.verbosity:
		verbosity = True
	else:
		verbosity = False
	
	source = args.source

	if args.filename:
		with open(source, newline='') as file:
			for row in file.readlines():
				passw = row.strip()
				check = check_pass(passw)
				if check:
					if verbosity:
						print('>>> PASSWORD MATCH! <<<')
						print('Password: ', passw)
						print('SHA1 Hash: ', check[0])
						print('Number of matches: ', check[1])
						print('-' * 20)
					else:
						print(passw)
				else:
					if verbosity:
						print('> Password {} is safu'.format(passw))
	else:
		check = check_pass(source)
		if check:
			if verbosity:
				print('>>> PASSWORD MATCH! <<<')
				print('Password: ', source)
				print('SHA1 Hash: ', check[0])
				print('Number of matches: ', check[1])
				print('-' * 20)
			else:
				print(source)
		else:
			if verbosity:
				print('> Password {} is safu'.format(source))

if __name__ == '__main__':
	main()