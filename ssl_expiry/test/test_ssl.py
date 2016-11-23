import unittest
from ssl_expiry.ssl_expiry import get_ssl_expiry

class QuickSSLTestCase(unittest.TestCase):

    def test_letsencrypt(self):
        date = get_ssl_expiry('letsencrypt.org')
        self.assertTrue('-' in date)
