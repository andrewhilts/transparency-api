#!/bin/bash
FILE=firstrun
source venv/bin/activate
printf "\n\n\n\n\nLaunching DIY Transparency application server. Please leave this window open throughout your use of the app.\n\n\n\n\n"
if [ -f $FILE ];
then
	virtualenv venv
	pip install -r requirements.txt
	rm $FILE
fi
python app.py