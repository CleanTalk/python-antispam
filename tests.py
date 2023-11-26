#!/usr/bin/python
# coding=utf-8

from __future__ import print_function
from cleantalk import CleanTalk
import os
import unittest
import json

class TestCleanTalk(unittest.TestCase):

    def setUp(self):
        # Make sure you have defined system environment variable 'CLEANTALK_TEST_API_KEY'.
        # Use your operating system tools or IDE tools to set this.
        self.ct = CleanTalk(auth_key=os.getenv('CLEANTALK_TEST_API_KEY'))

    def test_blacklisted(self):
        response = self.ct.request(
            message='abc',  # Comment visitor to the site
            sender_ip='196.19.250.114',  # IP address of the visitor
            sender_email='s@cleantalk.org',  # Email IP of the visitor
            sender_nickname='spam_bot',  # Nickname of the visitor
            post_info=json.dumps({'post_url': 'https://text.com/1/2/3/4.html'})
        )
        print(response)
        # make sure that 'allow' is 0
        self.assertFalse(response['allow'])

    def test_correct_ip(self):
        response = self.ct.request(
            message='Good text.',  # Comment visitor to the site
            sender_ip='127.0.0.1',  # IP address of the visitor
            sender_email='support@cleantalk.org',  # Email IP of the visitor
            sender_nickname='real human',  # Nickname of the visitor
            post_info = json.dumps({'post_url': 'https://text.com/1/2/3/4.html'})
        )
        print(response)
        self.assertTrue(response['allow'])

    def test_incorrect_email(self):
        response = self.ct.request(
            message='Good text.',  # Comment visitor to the site
            sender_ip='127.0.0.1',  # IP address of the visitor
            sender_email='sadasdas@cleaasdasdntalk.org',  # Email IP of the visitor
            sender_nickname='real human',  # Nickname of the visitor
            post_info=json.dumps({'post_url': 'https://text.com/1/2/3/4.html'})
        )
        print(response)
        self.assertTrue(bool(response['codes'].find('EMAIL_DOMAIN_NOT_EXISTS')))
        self.assertFalse(response['allow'])

    def test_incorrect_js_and_submit_time(self):
        response = self.ct.request(
            message='Good text.',  # Comment visitor to the site
            sender_ip='127.0.0.1',  # IP address of the visitor
            sender_email='good@cleantalk.org',  # Email IP of the visitor
            sender_nickname='aa-shi',  # Nickname of the visitor
            post_info=json.dumps({'post_url': 'https://text.com/1/2/3/4.html'})
        )
        print(response)
        self.assertTrue(bool(response['codes'].find('JS DISABLED')))
        self.assertTrue(bool(response['codes'].find('FAST_SUBMIT')))

    def test_js_null(self):
        # bad user
        response = self.ct.request(
            message='abc',  # Comment visitor to the site
            sender_ip='196.19.250.114',  # IP address of the visitor
            sender_email='stop_email@example.com',  # Email IP of the visitor
            sender_nickname='spam_bot',  # Nickname of the visitor
            post_info=json.dumps({'post_url': 'https://text.com/1/2/3/4.html'})
        )
        print(response)
        self.assertTrue(bool(response['codes'].find('JS DISABLED')))

        # good user
        response = self.ct.request(
            message='abc',  # Comment visitor to the site
            sender_ip='127.0.0.1',  # IP address of the visitor
            sender_email='s@cleantalk.org',  # Email IP of the visitor
            sender_nickname='aa-shi',  # Nickname of the visitor
            post_info=json.dumps({'post_url': 'https://text.com/1/2/3/4.html'})
        )
        print(response)
        self.assertTrue(bool(response['codes'].find('JS DISABLED')))
        self.assertFalse(response['allow'])


if __name__ == '__main__':
    unittest.main()
