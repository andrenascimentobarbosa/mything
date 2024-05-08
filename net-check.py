#!/usr/bin/python3 

# check connection with internet.

from requests import get

r = get('https://github.com/andrenascimentobarbosa/mything')

if r.status_code == 200:
    print('\033[1;32m[+] Connected\033[m')
else:
    print('\033[1;31mError:\033[m ', r.status_code)


