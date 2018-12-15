#!/usr/bin/env bash

for file in ../view_ui/*.ui; do
    name=`echo "$file" | cut -d '/' -f3 | cut -d '.' -f1`;
    destination="../view/$name.py";
    echo "$(pyuic5 ${file})" > ${destination};
    echo "Uaktualniono bądź utworzono plik: $name.py";
done