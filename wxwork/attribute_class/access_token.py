# -*- coding: utf-8 -*-
__author__ = 'gzp'

from wxwork.attribute_class.base import BaseAttr


class AccessToken(BaseAttr):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRECT'

    def get(self):
        return self._wxwork.get(url=self.url, params=dict(
            corpid=self._wxwork.corpid,
            corpsecret=self._wxwork.secret
        ))
