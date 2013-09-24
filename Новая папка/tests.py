#!/usr/bin/python
#coding=utf-8

from __future__ import print_function
from cleantalk import CleanTalk
import unittest


class TestCleanTalk(unittest.TestCase):

    def setUp(self):
        self.ct = CleanTalk(auth_key='7emegy4e')

    def test_blacklisted(self):
        response = self.ct.request(
            message = 'abc', # Comment visitor to the site
            sender_ip = '196.19.250.114', # IP address of the visitor
            sender_email = 'stop_email@example.com', # Email IP of the visitor
            sender_nickname = 'spam_bot', # Nickname of the visitor
            submit_time = 12, # The time taken to fill the comment form in seconds
            js_on = 1 # The presence of JavaScript for the site visitor, 0|1
        )
        print(response)
        #make sure that 'allow' is 0
        self.assertFalse(response['allow'])

    def test_correct_ip(self):
        response = self.ct.request(
            message = 'abc', # Comment visitor to the site
            sender_ip = '109.188.126.23', # IP address of the visitor
            sender_email = '', # Email IP of the visitor
            sender_nickname = 'spam_bot', # Nickname of the visitor
            submit_time = 12, # The time taken to fill the comment form in seconds
            js_on = 1 # The presence of JavaScript for the site visitor, 0|1
        )
        print(response)
        self.assertTrue(response['allow'])

    def test_correct_email(self):
        response = self.ct.request(
            message = 'abc', # Comment visitor to the site
            sender_ip = '', # IP address of the visitor
            sender_email = 'chelovek_cheloveku_volk@zombizombizombi.ru', # Email IP of the visitor
            sender_nickname = 'spam_bot', # Nickname of the visitor
            submit_time = 12, # The time taken to fill the comment form in seconds
            js_on = 1 # The presence of JavaScript for the site visitor, 0|1
        )
        print(response)
        self.assertTrue(response['allow'])

    def test_incorrect_js_and_submit_time(self):
        response = self.ct.request(
            message = 'abc', # Comment visitor to the site
            sender_ip = '', # IP address of the visitor
            sender_email = 'aa-shi@yandex.ru', # Email IP of the visitor
            sender_nickname = 'aa-shi', # Nickname of the visitor
            submit_time = 1, # The time taken to fill the comment form in seconds
            js_on = 0 # The presence of JavaScript for the site visitor, 0|1
        )
        print(response)
        self.assertFalse(response['allow'])

    def test_js_null(self):
        #bad user
        response = self.ct.request(
            message = 'abc', # Comment visitor to the site
            sender_ip = '196.19.250.114', # IP address of the visitor
            sender_email = 'stop_email@example.com', # Email IP of the visitor
            sender_nickname = 'spam_bot', # Nickname of the visitor
            submit_time = 12, # The time taken to fill the comment form in seconds
            js_on = None # The presence of JavaScript for the site visitor, 0|1
        )
        print(response)
        self.assertFalse(response['allow'])

        #good user
        response = self.ct.request(
            message = 'abc', # Comment visitor to the site
            sender_ip = '', # IP address of the visitor
            sender_email = 'aa-shi@yandex.ru', # Email IP of the visitor
            sender_nickname = 'aa-shi', # Nickname of the visitor
            submit_time = 12, # The time taken to fill the comment form in seconds
            js_on = None # The presence of JavaScript for the site visitor, 0|1
        )
        print(response)
        self.assertTrue(response['allow'])


if __name__ == '__main__':
    unittest.main()