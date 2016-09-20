#!/bin/sh


echo "Difficulty level :"$1
echo "Tests :"$2
echo

rm min.out ext.out
for run in $(seq $2)
do
    instance=$(./fetchsudoku.py $1)
    echo $instance

    ./minimal.py $instance 1>min.cnf
    ~/zchaff/zchaff min.cnf 1>min.tmp
    dnum=$(grep 'Num. of Decisions' min.tmp | awk -F'\t+' '{print $2}')
    rtime=$(grep 'Run Time' min.tmp | awk -F'\t+' '{print $2}')
    echo $dnum"\t"$rtime >> min.out

    ./extended.py $instance 1>ext.cnf
    ~/zchaff/zchaff ext.cnf 1>ext.tmp
    dnum=$(grep 'Num. of Decisions' ext.tmp | awk -F'\t+' '{print $2}')
    rtime=$(grep 'Run Time' ext.tmp | awk -F'\t+' '{print $2}')
    echo $dnum"\t"$rtime >> ext.out
done

rm min.cnf ext.cnf
rm min.tmp ext.tmp

echo "Done"
