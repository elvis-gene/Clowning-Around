Clowning Around
===============

There’s nothing quite as important as ensuring you’re punctual for any and all appointments made. This is a sign of respect and concern for the other parties time and needs. No being understands this quite as well as a clown. Your task, should you be so inclined, is to build a Django application, specifically for the time management needs of this world’s greatest child entertainers.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

The application, when complete, should be able to allow clowns, troupe leaders and clients to:

    Authenticate themselves as clowns, troupe leaders or clients

        - Clients to:

            - View their upcoming and past appointments (as an API endpoint)

            - Rate a past appointment with clown face emojis

        - Troupe leaders to:

            - Create appointments for clowns, assigned to a limited capacity troupe, managed by themselves

        - Clowns to:

            - View their appointments and change the current status of these appointments (upcoming, incipient, completed, cancelled)

            - Report an issue with an appointment (not a state change)

            - Request client contact details, with reason for request

All the above tasks should be completable through a collection of complete API endpoints. The application has a framework provided (based on https://github.com/pydanny/cookiecutter-django) with a fixture that contains dummy users you can use not only to test but also, use within your additional applications. The frontend provided can be ignored as a part of the cookiecutter and not the final application, which will be used exclusively through API endpoints. Your applications should include dummy data, which you can source from anywhere you’d like.

You only have two hours to complete the assignment, including any tasks you’d consider necessary to mark a feature/implementation/component complete. Should you not get around to doing anything, feel free to add TODO or NOTE comments to let us know you wanted to, but just didn’t get to.

Project Specific Note
---------------------

The following are some things to help you get started

To get the provided datadump.json file into your database


```docker-compose -f local.yml run --rm django python ./manage.py loaddata datadump.json```

(``https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata``)


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy clowning_around

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html



Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd clowning_around
    celery -A config.celery_app worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.




Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

.. _mailhog: https://github.com/mailhog/MailHog



Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



Project Specific Note
---------------------

The following are some things to help you get started

To get the provided datadump.json file into your database


```docker-compose -f local.yml run --rm django python ./manage.py loaddata datadump.json```

(``https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata``)
