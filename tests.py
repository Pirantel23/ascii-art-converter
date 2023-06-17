import unittest
import functions as fs
import os
from numpy import array_equal

class TestGrayscaleConversion(unittest.TestCase):
    def setUp(self):
        self.image = fs.read_image('samples/test_image.png')
        self.expected_grayscale = fs.read_image('samples/test_image_grayscale.png')
        self.expected_resized = fs.read_image('samples/test_image_resized.png')

    def test_grayscale(self):
        fs.save_image(fs.convert_to_grayscale(self.image), 'temp')
        actual_grayscale = fs.read_image('samples/temp.png')
        self.assertTrue(array_equal(actual_grayscale, self.expected_grayscale))


    def test_resize(self):
        fs.save_image(fs.resize_image(fs.convert_to_grayscale(self.image), (100,50)), 'temp')
        actual_resized = fs.read_image('samples/temp.png')
        self.assertTrue(array_equal(actual_resized, self.expected_resized))

    def tearDown(self):
        try:
            os.remove('samples/temp.png')
        except FileNotFoundError:
            pass
            

        
if __name__ == "__main__":
    unittest.main()