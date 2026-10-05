day=$(printf "day%02d" "$2")
for i in $(seq 1 "$1"); do
    mkdir -p "$day/$(printf "task%02d" "$i")"
done