import unittest
from socketClient import SocketClient

class TestSocketClient(unittest.TestCase):

    def test_connect(self):
        try:
            s = SocketClient()
            self.assertTrue(s.connect("www.google.com",80))
        finally:
            s.close()

if __name__ == '__main__':
    unittest.main()
