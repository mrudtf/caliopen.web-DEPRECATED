caliopen.web
============

CaliOpen Web Application


Installation
------------

This how-to is for installing caliopen for development purposes.

The backend requirements are currently:

 - redis (or memcache)
 - rabbitmq
 - elasticsearch
 - cassandra
 - python2.7 with virtualenv

Note that this documentation does not cover installing these products on your distro.

.. note::

    rabbitmq broker is optional depending on delivery mode set to direct or not
    in caliopen.yaml configuration.

Clone every component of caliopen.

::

    mkdir caliopen
    cd caliopen
    git clone https://github.com/CaliOpen/caliopen.config.git
    git clone https://github.com/CaliOpen/caliopen.core.git
    git clone https://github.com/CaliOpen/caliopen.messaging.git
    git clone https://github.com/CaliOpen/caliopen.smtp.git
    git clone https://github.com/CaliOpen/caliopen.storage.git
    git clone https://github.com/CaliOpen/caliopen.api.git
    git clone https://github.com/CaliOpen/caliopen.ng.git
    git clone https://github.com/CaliOpen/caliopen.web.git
    git clone https://github.com/CaliOpen/caliopen.cli.git

.. note::

    If you would like to submit pull requests, please fork the proper repo(s) and
    clone it (them) from your own github account.


Create a virtualenv and activate it.

::

    virtualenv venv
    source venv/bin/activate

    for d in caliopen.config caliopen.core caliopen.messaging caliopen.smtp caliopen.storage caliopen.api caliopen.web caliopen.cli
    do
      cd $d
      python setup.py develop
      
      if [ -e requirements.txt ] ; then
        pip install -r requirements.txt
      fi

      cd ..
    done


Compile angular app::

The web UI is built in AngularJS. It lives in its own repository.

::

    cd caliopen.ng
    source nactivate
    npm install
    bower install
    grunt build
    cd ..

.. note::

    "nactivate" is inspired by virtualenv to not use bower globally.
    Command ndeactivate will deactivate it.

    This is not mandatory, you can use bower the way you like.


Configure the caliopen website.

::

    cd caliopen.cli


Refer to caliopen.cli's README to set up storage, create a user
and import emails.



Run the web interface ::

    cd ..
    cd caliopen.web

    pserve development.ini
