import paramiko
import subprocess
import sys


ip_address = "bandit.labs.overthewire.org"
port = 2220
username = "bandit6"
password = "DXjZPULLxYr17uwoI01bNLQbtFemEgo7"

# ssh = subprocess.call(['ssh', username+"@" + ip_address, "-p", port])

# we know that the file is 1033 bytes and is a file
# and also we use filter for permissions and owner
# so we can use:
# cat $(find -type f -size 33c -user bandit7 -group bandit6 2>/dev/null)
# 2>/dev/null is to not show permission denied errors

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username,
                   password=password, port=port)

print('successfully connected')
ssh_client.invoke_shell()
stdin, stdout, stderr = ssh_client.exec_command(
    'cd / &&cat $(find -type f -size 33c -user bandit7 -group bandit6 2>/dev/null)')
print("flag: " + str(stdout.read(), 'utf-8'))

ssh_client.close()
