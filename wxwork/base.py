import logging
import requests


logger = logging.getLogger(__name__)


class BaseWxWork(object):

    def __init__(self, corpid, secret, retry=True):
        self.corpid = corpid
        self.secret = secret
        self.retry = retry

    def _request(self, url, **kwargs):
        method = kwargs.get('method', 'get')
        pass

    def get(self, url, **kwargs):
        if 'method' not in kwargs:
            kwargs['method'] = 'get'
        return self._request(url=url, **kwargs)

    def post(self, url, **kwargs):
        if 'method' not in kwargs:
            kwargs['method'] = 'post'
        return self._request(url=url, **kwargs)
