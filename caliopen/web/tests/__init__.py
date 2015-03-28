from __future__ import unicode_literals

import os

from caliopen.config import Configuration
from caliopen.core.config import includeme


# Core objects do need implmeentations to be registered
# If no implementation is registered, an exception is raised.

# This is required prior to any `caliopen.core` object inclusion

# This is a (ugly) way to have everything executed
# before the core objects imports

# Load config file
pwd = os.path.dirname(os.path.realpath(__file__))
DEFAULT_CONFIG_FILE = '%s/../../../caliopen.yaml' % pwd
Configuration.load(os.environ.get('CALIOPEN_CONFIG', DEFAULT_CONFIG_FILE),
        'global')

# register implmentations
includeme()
