import unittest

import minimart


class MinimartTestCase(unittest.TestCase):

    def setUp(self):
        self.app = minimart.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to minimart', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
