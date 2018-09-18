import inspect
import logging
import requests

from wxwork import attrs
from wxwork.attrs.base import BaseAttr
from wxwork.utils import camel_to_underline

logger = logging.getLogger(__name__)


def _attribute_classes():
    return [(name, member) for name, member in inspect.getmembers(attrs)
            if inspect.isclass(member) and issubclass(member, BaseAttr)]


class BaseWxWork(object):
    def __new__(cls, *args, **kwargs):
        self = super(BaseWxWork, cls).__new__(cls)

        for name, attribute in _attribute_classes():
            # formatting attribute to underline
            setattr(self, camel_to_underline(name), attribute(self))
        return self

    def __init__(self, corpid, secret, retry=True):
        self.corpid = corpid
        self.secret = secret
        self.retry = retry

    def _request(self, url, **kwargs):
        method = kwargs.pop('method', 'get')
        handler = getattr(requests, method)
        return handler(url=url, **kwargs)

    def get(self, url, **kwargs):
        if 'method' not in kwargs:
            kwargs['method'] = 'get'
        return self._request(url=url, **kwargs)

    def post(self, url, **kwargs):
        if 'method' not in kwargs:
            kwargs['method'] = 'post'
        return self._request(url=url, **kwargs)
