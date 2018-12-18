#!/usr/bin/env bash

for file in ../view_ui/*.ui; do
    name=`echo "$file" | cut -d '/' -f3 | cut -d '.' -f1`;
    destination="../TheGreatCartograph/view/$name.py";

    if [[ -e ${destination} ]]
    then
        echo "Uaktualniono plik: $name.py";
    else
        echo "Utworzono plik: $name.py";
    fi;

    echo "$(pyuic5 ${file})" > ${destination};
done