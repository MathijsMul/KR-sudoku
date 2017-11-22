#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters"
    echo "Usage: ./launch_test.sh difficulty_lv tests"
    exit
fi

encoding[0]=minimal
encoding[1]=extended
encoding[2]=hstrategies

echo "Difficulty level :"$1
echo "Tests :"$2
echo

run_test () {
    ./$1.py $2 1>$1.cnf
#<<<<<<< Updated upstream
    ../zchaff/zchaff $1.cnf 1>$1.tmp
    dlev=$(grep 'Decision Level' $1.tmp | gawk -F'\t+' '{print $2}')
    dnum=$(grep 'Num. of Decisions' $1.tmp | gawk -F'\t+' '{print $2}')
    rtime=$(grep 'Run Time' $1.tmp | gawk -F'\t+' '{print $2}')
    confcl=$(grep 'Added Conflict Clauses' $1.tmp | gawk -F'\t+' '{print $2}')
    conflt=$(grep 'Added Conflict Literals' $1.tmp | gawk -F'\t+' '{print $2}')
    impnum=$(grep 'Number of Implication' $1.tmp | gawk -F'\t+' '{print $2}')
#=======
    ../zchaff/zchaff $1.cnf 1>$1.tmp
    dlev=$(grep 'Decision Level' $1.tmp | awk -F'\t+' '{print $2}')
    dnum=$(grep 'Num. of Decisions' $1.tmp | awk -F'\t+' '{print $2}')
    rtime=$(grep 'Run Time' $1.tmp | awk -F'\t+' '{print $2}')
    confcl=$(grep 'Added Conflict Clauses' $1.tmp | awk -F'\t+' '{print $2}')
    conflt=$(grep 'Added Conflict Literals' $1.tmp | awk -F'\t+' '{print $2}')
    impnum=$(grep 'Number of Implication' $1.tmp | awk -F'\t+' '{print $2}')
#>>>>>>> Stashed changes
    echo -e $dlev"\t"$dnum"\t"$rtime"\t"$confcl"\t"$conflt"\t"$impnum>> $1.out
}



for run in $(seq $2)
do
    instance=$(python fetchsudoku.py $1)
    echo $instance

    for enc in "${encoding[@]}"
    do
        run_test $enc $instance
    done
done

for enc in "${encoding[@]}"
do
    echo
    echo $enc
    echo -e "\tdLv\tdNum\truntime\tconfcl\tconflt\timpnum"
    gawk -F$'\t' '{for (i=1;i<=NF;i++) sum[i]+=$i} END{ printf "Sum:"; for (i in sum) printf "\t%s", sum[i]; printf "\nAvg:"; for (i in sum) printf "\t%s", sum[i] / NR; printf "\n"}' $enc.out
    echo
    #rm $enc.cnf $enc.tmp
done

echo "Done"
