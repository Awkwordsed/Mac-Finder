#!/bin/bash

# Read the database file into an array
mapfile -t database < "data.csv"

echo "Only insert the first three parts of a MAC address (example, 00:00:00)"

# Prompt user for input
read -p "Enter MacAddress: " target

# Iterate through the lines in the database
for line in "${database[@]}"; do
    IFS=',' read -r macaddr vendid <<< "$line"

    if [ "$target" == "$macaddr" ]; then
        echo -e "$vendid"
        break
    fi
done
