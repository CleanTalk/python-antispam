#!/usr/bin/python
#coding=utf-8

from __future__ import unicode_literals
try:
    from urllib.request import urlopen, Request
    from urllib.parse import urlparse
    from urllib.parse import urlencode

except ImportError:
    from urllib2 import urlopen, Request
    from urlparse import urlparse
    from urllib import urlencode

import json


class CleanTalk:
    """Python API for CleanTalk.org"""
    VERSION = 1.2
    ENCODING = 'utf-8'
    user_agent = 'Mozilla/5.0'

    def __init__(self,
                 auth_key,
                 server_url = 'https://moderate.cleantalk.org',
                 api_url='/api2.0',
                 connection_timeout=8,
                 method_name='check_message',
                 agent = None):

        """
        This method constructs a new CleanTalk object and returns it.
        :param auth_key:
        :param server_url:
        :param api_url:
        :param connection_timeout:
        :param method_name:
        """
        self.__server_url = server_url
        self.__api_url = api_url
        self.__connection_timeout = connection_timeout
        self.__method_name = method_name
        self.__auth_key = auth_key
        if agent:
            self.__agent = agent
        else:
            self.__agent = 'python-api-' + str(CleanTalk.VERSION)

    def request(self, message, sender_ip, sender_email, sender_nickname, submit_time, js_on, post_info, example = '', method_name = None):
        """
        This method will dispatch call to servers.
        Exceptions can be raised: ValueError on bad json, URLError on bad url, HTTPError, HTTPException on http-error
        :param message: Comment visitor to the site
        :param example: The text of the article to which visitor created a comment
        :param sender_ip: IP address of the visitor
        :param sender_email: Email IP of the visitor
        :param sender_nickname: Nickname of the visitor
        :param submit_time: The time taken to fill the comment form in seconds
        :param js_on: The presence of JavaScript for the site visitor, 0|1
        :param method_name:
        :param post_info: info about the page
        :return: dictionary, where:
                    KEY                     VALUE
                -----------             --------------------
                allow                   0|1 - spam or not comment/registration
                id                      MD5_HEX - unique request ID
                comment                 string - description about request from server
                stop_queue              0|1 - should comment move to site's moderation queue or not
                inactive                0|1 - should registration move to inactive state or not
        """
        if not method_name:
            method_name = self.__method_name

        url = self.__server_url + self.__api_url
        headers = { 'User-Agent' : self.user_agent,
                    'content-type' :'application/json; encoding=utf-8' }

        values = {
            'auth_key': self.__auth_key,
            'method_name': method_name,
            'message': message,
            'example': example,
            'sender_ip': sender_ip,
            'sender_email': sender_email,
            'sender_nickname': sender_nickname,
            'submit_time': submit_time,
            'js_on': js_on,
            'agent': self.__agent,
            'post_info': post_info
        }
        data = json.dumps(values, separators=(',',':'))
        request = Request(url, data.encode(CleanTalk.ENCODING), headers)
        response = urlopen(request, timeout=self.__connection_timeout)
        response_bytes = response.read()
        response_str = response_bytes.decode(CleanTalk.ENCODING)
        response_parsed = json.loads(response_str)

        return response_parsed