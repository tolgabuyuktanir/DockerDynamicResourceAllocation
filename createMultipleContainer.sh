#!/bin/bash
for value in {1..32}
do
n=$((RANDOM%1000000+1000000))
docker run -d -m="5mb" --memory-swap="4096mb" number-sort python ./randomNumberSort.py $RANDOM $n
echo $n
done

