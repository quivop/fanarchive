#!/bin/bash

# set debug environment variable
if [ -z "$DEBUG" ] ; then
	DEBUG=False
else
	echo "-----> DEBUG variable already set. Moving on..."
fi	

# define secret key function
function mk_secret_key () {
	python manage.py shell -c "from django.core.management import utils; print(utils.get_random_secret_key())"
} 

# If a secret key exists...
if [ -z "$SECRET_KEY"] ; then
	echo `SECRET_KEY=$(mk_secret_key)`
# Make a new key and stuff it into heroku's mouth:
else
	echo "-----> Secret key already set. Moving on..."
fi

# run database migrations
echo "-----> Running db migrations..."
echo `python manage.py migrate`
