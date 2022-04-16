Create a virtual environment:

.. code-block:: bash

    $ python3 -m venv venv

    enter "venv\Scripts\activate" command on Windows
    enter "source venv/bin/activate" command on MacOS


Install requirements
---------------

Install all the necessary libraries using the following command

.. code-block:: bash

    $ pip install -r requirements.txt

Create a superuser:
-------------------
.. code-block:: bash

    $ python manage.py createsuperuser

Finally, run "python manage.py makemigrations" and "python manage.py migrate" commands to create a db.sqlite3 database

Run local server:
    python manage.py runserver
