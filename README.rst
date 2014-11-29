caliopen.web
============

caliopen web application.


Installation
------------

This install is about how to install caliopen for a development usage.

Currently, the minimum backend requirements is:

 - redis (or memcache)
 - rabbitmq
 - elasticsearch
 - cassandra
 - python2.7 with virtualenv

This documentation don't cover how to install those products on your distro.

.. note::

    rabbitmq broker is optional depending on delivery mode set to direct or not
    in caliopen.yaml configuration.

Then you have to clone every component of caliopen.

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

    if you want to create pull request you should fork component and
    clone from your own github account.


Then you should create virtualenv and activate it.

::

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

The web ui has been developed using AngularJS and live in it's own
repository.

::

    cd caliopen.ng
    source nactivate
    npm install
    bower install
    grunt build
    cd ..

..note::

    "nactivate" is inspired by virtualenv to don't use bower globally. 
    the command ndeactivate will deactivate it.

    This is not mandatory, you can use the way you use bower if you
    prefer.


Configure the caliopen website.

::

    cd caliopen.cli


Refer to caliopen.cli README instruction to setup storage, create an user
and import emails



Run the web interface ::

    cd ..
    cd caliopen.web

    pserve development.ini
