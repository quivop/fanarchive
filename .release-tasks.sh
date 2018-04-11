#!/bin/bash

# set environment variables
DEBUG=False

SECRET_KEY="fakekey" # set because Django whines if you don't 

# define secret key function
function mk_secret_key () {
	python manage.py shell -c "from django.core.management import utils; print(utils.get_random_secret_key())"
} 

# Make a new key and stuff it into heroku's mouth:
echo `heroku config:set SECRET_KEY=$(mk_secret_key)`

# run database migrations
echo "Running db migrations..."
echo `python manage.py migrate`

# notify user re how to load data
"To load sample data into the app, type './.loaddata' into your shell, and press enter."

# # load test data from fixtures
# echo -e "Do you want to load test data into the archive?\\n
# Type 'y' for yes, or 'n' for no: \c"
# read answer

# if [[ $answer -eq 'y' ]] ; then
# 	echo `python manage.py loaddata fanarchive\fixtures\initial_data.json`
