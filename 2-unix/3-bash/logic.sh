# !/bin/bash
for i in {1..10}; do 
    echo "Welcome $i times"
done

read -p "Insert a number": MYVAR

if [ $MYVAR -gt 10 ]; then
    echo "myvar is greater than 10"
else
    echo "myvar is 10 or less"
fi

if [ $MYVAR -gt 2 ] && [ $MYVAR -lt 10 ]; then
    echo "myvar is between 2 and 10"
fi

echo "What asset do you want to enter?"
read ASSET

if [ "$ASSET" = "SPX" ]; then
    echo "Asset selected is SPX500" $ASSET
elif [ "$ASSET" = "DXY" ]; then
    echo "Asset selected is Dollar" $ASSET
else
    echo "${ASSET} not contained in log"
fi

declare -a array=("GOLD" "XAU" "XBT")

for i in "${array[@]}"
do
    echo "This ${i} has volatility above average"
done

echo "How many Loops do you Want ?"
read LOOPS

COUNT=1
while [ $COUNT -le $LOOPS ]
do 
    echo $COUNT "before increment"
    echo "Loop# $COUNT "
    ((COUNT++))
    echo $COUNT "after increment"
done

touch one.txt\
    && touch two.txt\
    && touch three.txt &&
    # Count the files created
    ls *.txt | wc -l

ls -l fake-file.txt &> /dev/null && echo "worked"

false && echo "also don't work"
true && echo "will work"
false || echo "Run this instead"
echo "Run this but not that" || echo "This won't run"

#!/usr/bin/env bash
for filename in file{1..10};
    do
        echo "Filename: $filename" > $filename.txt
    done 


for filename in file{1..10};
    do
        rm $filename.txt
    done

files=(/etc/hosts /etc/profile /etc/bashrc)

for file in "${files[@]}"; do
    ls -l "$file"
done

function preview_file() {
    read -p "Enter a file to preivew" FILE
    head -n 5 FILE
    tail -n 5 FILE
}

# Array and Hash
declare -a array=("apple" "pear" "cherry")

for i in "${array[@]}";
    do 
        echo "This ${i} is delicious!"
    done

declare -A mealhash=([dinner]="steak" [lunch]="salad" [breakfast]="fruit")

for key in "${!mealhash[@]}"; 
    do
        echo "For $key I like to eat: ${mealhash[$key]}"
    done