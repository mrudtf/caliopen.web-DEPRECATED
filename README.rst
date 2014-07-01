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

.. note::

    if you want to create pull request you should fork component and
    clone from your own github account.


Then you should create virtualenv and activate it.

::

    source venv/bin/activate

    for d in caliopen.config caliopen.core caliopen.messaging caliopen.smtp caliopen.storage caliopen.api caliopen.web
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

    cd caliopen.web


Copy the sample development.ini file to roll your own configuration parameters::

    cp development.ini.sample development.ini


Setup the storage database::

    caliopen -f development.ini.sample setup


Create a user::

    caliopen create_user --help
    caliopen -f development.ini create_user -e imported@email -p password -f firstname -l lastname


Then import a mailbox ::

    caliopen import --help
    caliopen -f development.ini.sample import -p ~/gandiv4 -e  imported@email -f maildir


.. note::

    This will push message in the rabbitmq broker if direct keyword is set to False
    in delivery_agent configuration section.



Run the delivery agent ::

    python caliopen/web/bin/deliver.py -f development.ini


.. note::

    Only apply if direct set to False in delivery_agent configuration section.

    Currently the delivery agent consume message over rabbitmq.
    The delivery aims to be a daemon but for developer it run in it's own
    terminal.
    You can shutdown with ctrl-c when your rabbitmq queue is empty


Run the web interface ::

    pserve development.ini
