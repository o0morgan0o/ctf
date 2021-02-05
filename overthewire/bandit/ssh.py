import subprocess
import sys

password = "cvX2JJa4CFALtqS87jk27qwqGhBM9plV"

ssh = subprocess.call(
    ['ssh', "bandit8@bandit.labs.overthewire.org", "-p", "2220"])
