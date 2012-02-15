# -*- coding:utf-8 -*-
try:
    from django.utils.log import RequireDebugFalse
except ImportError:
    import logging
    from django.conf import settings

    class RequireDebugFalse(logging.Filter):
        def filter(self, record):
            return not settings.DEBUG
