automoxapi
=======

A thin python wrapper for the Automox API

Usage
-----

Log into Automox, navigate to settings and locate and copy the Access Key.

In your python environment, install automoxapi:

.. code:: bash

    pip install automoxapi

In your python project import and create an Automox instance:

.. code:: python


    from automoxapi import Automox

    automox = Automox('thisis-not-areal-accesskey')

    for org in automox.get_organizations():
        for server in automox.get_servers(org['id']):
            print(server['display_name'])



For details on interacting with the API visit the website:
https://docs.automox.com/api/