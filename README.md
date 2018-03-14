**Django Rest Framework Serializer Examples**

I recommend that you install virtualenv and make a virtual environment for installing the Python requirements in this project.

To install:
	pip -r requirements.txt

This project was started by following:

	https://docs.djangoproject.com/en/1.11/intro/install/

	http://www.django-rest-framework.org/#installation

I renamed the configuration directory from ExamineDRFSerializers to config because I think it is clearer what is going on when the project gets more complicated.

Then run python manage.py migrate

	This creates a SQLlite file for the database

Then run python.manage.py runserver

	This starts the server running at http://localhost:8000 as long as you leave the command running in the terminal window you started it in



