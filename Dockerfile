FROM debian:wheezy

RUN apt-get update

# Install python
RUN     apt-get install -y \
      python2.7 \
      python-setuptools \
      python-dev \
      python-pip \
      libffi-dev \
      git


# Import python app
## Prepare ssh environment
ADD . /srv/caliopen.web


WORKDIR /srv/caliopen.web

# Copy configuration
ADD  https://raw.githubusercontent.com/CaliOpen/caliopen.base/master/caliopen.yaml.template caliopen.yaml

VOLUME ['/srv/caliopen.web']


# Install caliopen dependencies
RUN     pip install -U pip     # use a decent version
RUN pip install git+https://github.com/Caliopen/caliopen.base.git
RUN pip install git+https://github.com/Caliopen/caliopen.base.user.git
RUN pip install git+https://github.com/Caliopen/caliopen.base.message.git
RUN pip install git+https://github.com/Caliopen/caliopen.api.base.git
RUN pip install git+https://github.com/Caliopen/caliopen.api.user.git
RUN pip install git+https://github.com/Caliopen/caliopen.api.message.git

# Install
RUN     python setup.py install
RUN     python setup.py develop

# install development extra
RUN     pip install -e ".[dev]"  # installed development tools if any

RUN     useradd docker

EXPOSE 6543


CMD [ "pserve", "development.ini.sample" ]
