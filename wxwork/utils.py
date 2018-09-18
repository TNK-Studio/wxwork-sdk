# -*- coding: utf-8 -*-
__author__ = 'gzp'


def camel_to_underline(camel_format):
    """
    驼峰命名格式转下划线命名格式
    :param camel_format:
    :return:
    """
    underline_format = ''
    if isinstance(camel_format, str):
        for _s_ in camel_format:
            underline_format += _s_.lower() if _s_.islower() or not underline_format else '_' + _s_.lower()
    return underline_format


def underline_to_camel(underline_format):
    """
    下划线命名格式驼峰命名格式
    :param underline_format:
    :return:
    """
    '''
    '''
    camel_format = ''
    if isinstance(underline_format, str):
        for _s_ in underline_format.split('_'):
            camel_format += _s_.capitalize()
    return camel_format
