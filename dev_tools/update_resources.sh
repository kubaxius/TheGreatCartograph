#!/usr/bin/env bash

cd ../resources/images
destination="../../TheGreatCartograph/resources"

# iterating over all directories in ../resources/images
for dir in `find . -maxdepth 1 -mindepth 1 -type d -printf '%f\n'`; do

    # searching for qrc file
    qrc_name=$(find ${dir} -name *.qrc -printf '%f\n');

    # creating name for new py file
    py_name="$(echo "$qrc_name" | cut -d '.' -f1).py";

    # checking if this file exists and echoing appropriate message
    if [[ -e ${destination}/${py_name} ]]
    then
        echo "Updated resource: $py_name";
    else
        echo "Created resource: $py_name";
    fi;

    # creating file
    $(pyrcc5 -o "$destination/$py_name" "${dir}/${qrc_name}")
done