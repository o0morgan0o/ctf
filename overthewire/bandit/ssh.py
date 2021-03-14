import subprocess
import sys
import passwords

password = "truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk"
pass = passwords.ban

ssh = subprocess.call(
    ['ssh', "bandit10@bandit.labs.overthewire.org", "-p", "2220"])
:w
