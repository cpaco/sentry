from __future__ import absolute_import

from .base import *  # NOQA
from .manager import IntegrationManager  # NOQA
from .view import *  # NOQA


default_manager = IntegrationManager()
all = default_manager.all
get = default_manager.get
exists = default_manager.exists
register = default_manager.register
unregister = default_manager.unregister
