from pyramid.config import Configurator

from .config import includeme  # used by pyramid
from caliopen.base.config import Configuration

__version__ = '0.0.1'


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # XXX ugly way to init caliopen configuration before pyramid
    caliopen_config = settings['caliopen.config'].split(':')[1]
    Configuration.load(caliopen_config, 'global')

    config = Configurator(settings=settings)
    config.end()
    return config.make_wsgi_app()
