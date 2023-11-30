__version__ = "1.0.0a0"


from .webserver import Webserver
from .routes import Routes

def setup(set_prefix=True):
    """
    Configure the settings (this happens as a side effect of accessing the
    first setting), configure logging and populate the app registry.
    Set the thread-local urlresolvers script prefix if `set_prefix` is True.
    """
    import castanett.apps
    import castanett.config
    import castanett.initialize
    import castanett.command
    import castanett.helper
    import castanett.management
    import castanett.application
    import castanett.core
    import castanett.http
    import castanett.implement
    import castanett.security
    import castanett.session
