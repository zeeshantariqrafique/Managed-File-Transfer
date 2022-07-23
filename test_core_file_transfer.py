import unittest
import os
from core_file_transfer import PythonFileTransfer

class TestPythonFileTransfer(unittest.TestCase):
    def setUp(self) -> None:
        self.file_to_be_compressed = 'test.txt'
        self.test_file = open(self.file_to_be_compressed,'w+')
        self.expected_compressed_file_name = 'test.txt.gz'

    def test_compress_file(self) -> None:
        pyft = PythonFileTransfer()
        for line_number in range(10000):
            self.test_file.write(f'This is line number : {line_number}')
        compressed_file_name = pyft.compress_file(self.file_to_be_compressed)
        self.assertEqual(compressed_file_name,self.expected_compressed_file_name)

    def test_decompress_file(self):
        pyft = PythonFileTransfer()
        test_str = 'This is a test string'
        self.test_file.write(test_str)
        compressed_file_name = pyft.compress_file(self.file_to_be_compressed)
        decompressed_file_name = pyft.decompress_file(compressed_file_name,self.test_file)
        print(f'Decompressed file name is {decompressed_file_name}')

    def tearDown(self) -> None:
        self.test_file.close()
        os.remove(self.file_to_be_compressed)
        os.remove(self.expected_compressed_file_name)

if __name__ == '__main__':
    unittest.main()
