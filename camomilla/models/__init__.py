from camomilla.context.autodiscover import autodiscover_context_files
from .article import *  # NOQA
from .content import *  # NOQA
from .media import *  # NOQA
from .page import *  # NOQA
from .menu import *  # NOQA


def handle_context_registraion():
    autodiscover_context_files()
