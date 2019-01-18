# checkpass

Checks pwnedpasswords.com (https://haveibeenpwned.com/Passwords) for pwned passwords...

## Dependencies

Python 3

[Requests](http://docs.python-requests.org/en/master/)

## Usage

Checks pwnedpasswords.com for pwned passwords

positional arguments:

  source           filename or password to check

optional arguments:

  -h, --help       show this help message and exit

  -f, --filename   use an optional .txt sourcefile. One password per line

  -s, --silence  decreases verbosity


### Default mode 

`python check_passwd.py PASSWORD`


### File mode ([-f FILENAME])

`python check_passwd.py -f example.txt`

Pass a .txt file with one password per line to check password in bulk.

### Silent mode

`python check_passwd.py -s example.txt`

If the flag -s is used, the script will only print out pwned passwords.

