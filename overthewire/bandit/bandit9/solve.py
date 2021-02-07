import paramiko
import subprocess
import sys


ip_address = "bandit.labs.overthewire.org"
port = 2220
username = "bandit9"
password = "UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR"

# ssh = subprocess.call(['ssh', username+"@" + ip_address, "-p", port])

# we can make a grep on the strings of the file
# can't make a awk version of this, it doesn't work, dont' know why

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username,
                   password=password, port=port)

print('successfully connected')
ssh_client.invoke_shell()
stdin, stdout, stderr = ssh_client.exec_command(
    'strings data.txt | grep "==*" ')
print("flag: " + str(stdout.read(), 'utf-8'))

ssh_client.close()
