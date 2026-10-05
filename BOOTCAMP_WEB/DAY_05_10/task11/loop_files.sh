for file in *.md; do
    [ -f "$file" ] || continue
    echo "This is a new line." >> "$file"
done