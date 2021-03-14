import subprocess
import paramiko
import os
import sys
from .. import passwords

host = "leviathan.labs.overthewire.org"
username = "leviathan2"
password = passwords.password2
port = 2223
print("----------------------------")
print("password for ssh is : " + password)
print("run: ssh " + username + "@" + host + " -p " + str(port))
print("----------------------------")

# Utiliser ltrace pour voir le string compare dans le programme, ensuite on peut simplement aller lire le pass dans /etc/leviathan_pass/leviathan2

# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname=host, username=username,
#                    password=password, port=port)

# print('successfully connected')
# ssh_client.invoke_shell()
# stdin, stdout, stderr = ssh_client.exec_command(
#     'cat .backup/bookmarks.html | grep password')
# print(str(stdout.read(), 'utf-8'))

# ssh_client.close()
