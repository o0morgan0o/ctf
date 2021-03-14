#!/bin/bash
key="FREKEY"
# 5 17 4 10 4 24
n=0
for letter in $(cat $1);
do
    if [[ $n == 6 ]];
        then n=0;
    fi;
    # echo $n
    tmp="."
    
    if  (($n == 0)) ;
    then tmp=$(echo $letter | tr "F-ZA-E" "A-Z");

    elif (($n == 1));
    # then tmp=$(echo $letter | tr "R-ZA-Q" "A-Z");
    then tmp=".";

    elif (($n == 2));
    then tmp=$(echo $letter | tr "E-ZA-D" "A-Z");

    elif (($n == 3));
    then tmp=$(echo $letter | tr "K-ZA-J" "A-Z");

    elif (($n == 4));
    then tmp=$(echo $letter | tr "E-ZA-D" "A-Z");

    elif (($n == 5));
    then tmp=$(echo $letter | tr "Y-ZA-X" "A-Z");
    # else tmp=".";

    else tmp=".";
    fi;
    n=$(($n+1))
    VAR+=$tmp
done;
echo "$VAR"
# ;