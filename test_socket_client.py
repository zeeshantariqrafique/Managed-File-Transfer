import unittest
from socket_client import SocketClient

class TestSocketClient(unittest.TestCase):

    def test_connect(self):
        try:
            s = SocketClient()
            self.assertTrue(s.connect("www.google.com",80))
        except:
            print('No internet connection')
        finally:
            s.close()

if __name__ == '__main__':
    unittest.main()
