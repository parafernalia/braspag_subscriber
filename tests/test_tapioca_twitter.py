# coding: utf-8

import unittest

from tapioca_twitter import Twitter


class TestTapioca(unittest.TestCase):

    def setUp(self):
        self.wrapper = Twitter(
            api_key='api_key',
            api_secret='api_secret',
            access_token='access_token',
            access_token_secret='access_token_secret')

    def test_resource_access(self):
        resource = self.wrapper.statuses_mentions_timeline()

        self.assertEqual(resource.data(), 'https://api.twitter.com/1.1/statuses/mentions_timeline.json')


if __name__ == '__main__':
    unittest.main()
