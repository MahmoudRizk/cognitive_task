sample_django
==============

A service with both GUI & API interfaces built with Python, Django & FusionCharts.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


Getting Started
---------------
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Prerequisites
^^^^^^^^^^^^^
Requires Python3.6+ & PostgreSQL.

Linux (Ubuntu)
~~~~~~
::

  $ sudo apt-get install postgresql postgresql-contrib

Create a user to be used later when connecting django with the database.

Environment variables settings
^^^^^^^^^^^^^

**Set database url:**

::

  DATABASE_URL=postgres://username:password@127.0.0.1:5432/databasename.

**Set admin url:**

::

  DJANGO_ADMIN_URL="admin/"

**Set AWS keys:**

Since we are not using AWS for storage nor for staticfiles, so we set these variables to None.
::

    DJANGO_AWS_ACCESS_KEY_ID=None
    DJANGO_AWS_SECRET_ACCESS_KEY=None
    DJANGO_AWS_STORAGE_BUCKET_NAME=None


**Set django secret key:**

::
    
    DJANGO_SECRET_KEY="key"

**Set MailGun:**
::
    MAILGUN_API_KEY=None
    MAILGUN_DOMAIN=None

For more settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html


Installing
^^^^^^^^^^^^^
Install all the requirements:
::

  $ pip install -r requirements.txt

Migrate the database:
::

  $ python manage.py migrate

Run the server:
::

  $ python manage.py runserver

Setting Up Your Users
~~~~~~~~~~~~~~~~~~~~~~~~~~

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser


API
----------

The API enables to view, create, delete & update the database. The API is not using any type of authentication to make it simple and easy to test.


Get API:
^^^^^^^^^^^^^
Returns all entries in the database.

Resource URL
~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    https://sample-django-123.herokuapp.com/campaign/api/

Resource Information
~~~~~~~~~~~~~~~~~~~~~~~~~~
    
+----------------------------+-----------+
| Response formats           |   JSON    | 
+----------------------------+-----------+
| Requires authentication?   |   No      |  
+----------------------------+-----------+

keys
~~~~~~~~~~~~~~~~~~~~~~~~~~
+------------+---------------------------+
| Name       | Description               |
+============+===========================+
| id         | database unique id        | 
+------------+---------------------------+
| name       | name of the campaign      |  
+------------+---------------------------+
| country    | country's name            |  
+------------+---------------------------+
| budget     | campaign's budget         |  
+------------+---------------------------+
| goal       | campaign's goal           |  
+------------+---------------------------+
| category   | category of campaign      |  
+------------+---------------------------+

Example Requests
~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    $ curl --request GET --url 'https://sample-django-123.herokuapp.com/campaign/api/'


Example Response
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    
  [{
    "id": 20,
    "name": "n2",
    "country": "USA",
    "budget": 399,
    "goal": "Conversion",
    "category": "Sports"
  },
  {
    "id": 21,
    "name": "n3",
    "country": "EGY",
    "budget": 149,
    "goal": "Awareness",
    "category": "Sports"
  },
  {
    "id": 19,
    "name": "aaaaa",
    "country": "FR",
    "budget": 149,
    "goal": "rrr",
    "category": "Sports"
  },
  {
    "id": 22,
    "name": "n99",
    "country": "FR",
    "budget": 324,
    "goal": "Awareness",
    "category": "Sports"
  }]

Create API:
^^^^^^^^^^^^^
Create an entry in the datanase.

Resource URL
~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    https://sample-django-123.herokuapp.com/campaign/api/create/

Resource Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------+-----------+
| Response formats           |   JSON    | 
+----------------------------+-----------+
| Requires authentication?   |   No      |  
+----------------------------+-----------+

keys
~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+---------------------------+------------+
| Name       | Description               | Required   |
+============+===========================+============+
| id         | database unique id        | False      |
+------------+---------------------------+------------+
| name       | name of the campaign      | True       |
+------------+---------------------------+------------+
| country    | country's name            | True       |
+------------+---------------------------+------------+
| budget     | campaign's budget         | True       |
+------------+---------------------------+------------+
| goal       | campaign's goal           | True       |
+------------+---------------------------+------------+
| category   | category of campaign      | True       |
+------------+---------------------------+------------+


Example Requests
~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    $ curl --header "Content-Type: application/json"\
           --request POST \
           --data '{"name":"xyz","country":"EGY","budget":"199","goal":"Awareness","category":"Sports"}' \
           https://sample-django-123.herokuapp.com/campaign/api/create/

Example Response
~~~~~~~~~~~~~~~~~~~~~~~~~~
::
    
    {
      "id": 25,
      "name": "xyz",
      "country": "EGY",
      "budget": 199,
      "goal": "Awareness",
      "category": "Sports"
    }

Testing
----------

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test campaign
    $ coverage html
    $ open htmlcov/index.html
