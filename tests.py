#!/usr/bin/python
#coding=utf-8

from __future__ import print_function
from cleantalk import CleanTalk
import unittest


class TestCleanTalk(unittest.TestCase):

    def setUp(self):
        self.ct = CleanTalk(auth_key='7emegy4e')

    def test_blacklisted(self):
        response = self.ct.request(message = 'abc',
                                sender_ip = '196.19.250.114',
                                sender_email = 'stop_email@example.com',
                                sender_nickname = 'spam_bot',
                                submit_time = 12,
                                js_on = 1)

        print (response)
        #make sure that response contain 'allow'
        self.assertTrue('allow' in response)
        #make sure that 'allow' is true
        self.assertFalse(response['allow'])


if __name__ == '__main__':
    unittest.main()