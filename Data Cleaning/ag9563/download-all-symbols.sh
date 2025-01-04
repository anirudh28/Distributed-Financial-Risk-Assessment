mkdir stocks
while read -r line; do
    TICKER=$line python3 download-symbol.py
    sleep 1
done < symbols.txt