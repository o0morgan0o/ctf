import subprocess
import sys

password = "UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK"

ssh = subprocess.call(
    ['ssh', "bandit3@bandit.labs.overthewire.org", "-p", "2220"])
