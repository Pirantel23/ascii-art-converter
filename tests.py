import unittest
import numpy as np
import functions as fs
import os

class TestGrayscaleConversion(unittest.TestCase):
    def setUp(self):
        self.image = fs.read_image('samples/test_image.png')
        self.grayscale = fs.read_image('samples/test_image_grayscale.png')


    def test_grayscale_fast(self):
        expected_grayscale = fs.read_image('samples/test_image_grayscale.png')
        fs.save_image(fs.convert_to_grayscale(self.image, True), 'temp')
        actual_grayscale = fs.read_image('samples/temp.png')
        self.assertTrue(np.array_equal(actual_grayscale, expected_grayscale))


    def test_grayscale_slow(self):
        expected_grayscale = fs.read_image('samples/test_image_grayscale.png')
        fs.save_image(fs.convert_to_grayscale(self.image, False), 'temp')
        actual_grayscale = fs.read_image('samples/temp.png')
        self.assertTrue(np.array_equal(actual_grayscale, expected_grayscale))


    def test_resize(self):
        expected_resized = fs.read_image('samples/test_image_resized.png')
        fs.save_image(fs.resize_image(self.grayscale, (100,50))/255, 'temp')
        actual_resized = fs.read_image('samples/temp.png')
        self.assertTrue(np.array_equal(actual_resized, expected_resized))

    def tearDown(self):
        try:
            os.remove('samples/temp.png')
        except FileNotFoundError:
            pass
            

        
if __name__ == "__main__":
    unittest.main()