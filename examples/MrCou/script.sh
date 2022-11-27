for var in "$@"
do
    python3 Wikipedia.py $var > "$var".txt
    echo "Created file "$var".txt"
done