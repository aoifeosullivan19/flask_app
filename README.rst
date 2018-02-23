=========
flask_app
=========


This project creates a simple Flask application which displays the platform information of the machine you are running the app on. 


* Free software: GNU General Public License v3


Project Setup
--------

Please follow these instructions in order to configure the flask_app on your machine. 

1. It is recommended that you use a virtualenv to install Flask and run this application on. Using a virtualenv allows you to use different versions of Python for different projects in their own isolated development environments. Please follow the link below for more detailed information on installing and creating your own virtual environment.

http://docs.python-guide.org/en/latest/dev/virtualenvs/

2. You will need to install Flask, either on your virtualenv or system-wide, in order to run the flask_app. If you are installing on your virtualenv, you can use the following command:
        pip install Flask

However, if installing across your whole system you should use:
        sudo pip install Flask

This link provided more information on Flask and it's installation: http://flask.pocoo.org/docs/0.12/installation/

3. Before you can use the flask_app, you will need to install the systeminfo project from Github using pip install:
        pip install git+https://github.com/aoifeosullivan19/systeminfo1.git
        
This simple module reads the platform and system information from your machine. 

4. Next you will need to clone the flask_app repository from Github. If you do not already have Git installed by default, please install Git (https://git-scm.com). Navigate to the directory where you want to store this folder and use the following command:
        git clone https://github.com/aoifeosullivan19/flask_app.git
The flask_app will now be downloaded on to your system and ready for use. 

5. Navigate into the flask_app directory and to run this application and display your system information, use the following command:
        python run.py
        
Your platform information will now be displayed on http://0.0.0.0:5000. 

Authors
-------
Aoife O'Sullivan

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
