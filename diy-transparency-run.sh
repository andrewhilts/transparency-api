#!/bin/bash
SCRIPTPATH=${BASH_SOURCE[${#BASH_SOURCE[@]} - 1]}
DIRECTORY=$(dirname "${SCRIPTPATH}")
cd "${DIRECTORY}"
source venv/bin/activate
printf "\n\n\n\n\nLaunching DIY Transparency application server. Please leave this window open throughout your use of the app.\n\n\n\n\n"
python app.py