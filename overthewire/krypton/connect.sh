#!/bin/bash
level1="KRYPTONISGREAT"
level2="ROTTEN"
level3="CAESARISEASY"
level4="BRUTE"
level5="CLEARTEXT"

user="krypton5"

# echo $level0
echo 'sshpass -p '  $level5 'ssh ' $user '@krypton.labs.overthewire.org -p 2231'
sshpass -p $level5 ssh $user@krypton.labs.overthewire.org -p 2231


# ================
# level 1
# use a command to rot13 automatically
# alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"
# ================

