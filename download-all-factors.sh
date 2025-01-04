mkdir factors
while read -r line; do
    TICKER=$line python3 download-factor.py
    sleep 1
done < factors.txt
