import paramiko
import subprocess
import sys


ip_address = "bandit.labs.overthewire.org"
port = 2220
username = "bandit0"
password = "bandit0"

# ssh = subprocess.call(['ssh', username+"@" + ip_address, "-p", port])

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username,
                   password=password, port=port)

print('successfully connected')
ssh_client.invoke_shell()
stdin, stdout, stderr = ssh_client.exec_command('cat readme')
print(str(stdout.read(), 'utf-8'))

ssh_client.close()
