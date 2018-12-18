#!/usr/bin/env bash

for file in ../TheGreatCartograph/view/*.py; do
    name=`echo "$file" | cut -d '/' -f4 | cut -d '.' -f1`;
    destination="../view_ui/$name.ui";

    if [[ ! -e ${destination} ]]
    then
        "$(rm ${file})";
        echo "Usunięto plik: $name.py";
    fi;

done