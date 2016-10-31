#coding=utf-8
import unittest
import requests


class RequestBase(object):


    def get(self, url, *args, **kwargs):
        return requests.get(url, *args, **kwargs)

    def post(self, url, *args, **kwargs):
        return requests.post(url, *args, **kwargs)


class PollsTest(unittest.TestCase, RequestBase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000'


    def tearDown(self):
        pass


    def test_get_poll_index(self):
        data = {'a':1, 'b': 2}
        r = self.get(self.base_url, data)
        code = r.status_code
        text = r.text
        self.assertEqual(code, 200)


    def test_get_info(self):
        r = self.get(self.base_url)
        code = r.status_code
        text = r.text
        self.assertEqual(code, 200)
        self.assertIn('3', text)


if __name__ == '__main__':
    
    unittest.main()