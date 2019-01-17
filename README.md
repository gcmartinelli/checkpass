# checkpass

Checks pwnedpasswords.com (https://haveibeenpwned.com/Passwords) for pwned passwords...

## Dependencies

(Requests)[http://docs.python-requests.org/en/master/]

## Usage

Checks pwnedpasswords.com for pwned passwords

positional arguments:

  source           filename or password to check

optional arguments:

  -h, --help       show this help message and exit

  -f, --filename   use an optional .txt sourcefile. One password per line

  -v, --verbosity  increase verbosity


### Default mode 

`python check_passwd.py PASSWORD`

*By default script will only return passwords that have been pwned*

### File mode ([-f FILENAME])

`python check_passwd.py -f example.txt`

Pass a .txt file with one password per line to check password in bulk.

### Verbose mode

`python check_passwd.py -v example.txt`

If the flag -v is used, the script will give more details, in terminal, about each password passed. 

