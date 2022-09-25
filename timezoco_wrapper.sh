#!/bin/bash
if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python3 -m pip install --user --upgrade pip #installs pip - required for installing other packages
        python3 -m venv .venv #creates virtual environment
        source .venv.sh #activates virtual environment
        python3 -m pip install simple-term-menu #installs simple term menu package
        python3 -m pip install pytz #installs pytz package
        python3 main.py #runs the application

    else
        -x "$(command pip3 install --upgrade pip"

        echo "Python $pyv is an older version! This program needs the latest version.
    You can get it here - https://www.python.org/downloads/" >&2
    fi 
else
    echo "Looks like you don't have Python installed.
        You can download it here - https://www.python.org/downloads/" >&2
fi