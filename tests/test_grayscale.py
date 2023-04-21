import unittest
from PIL import Image
import numpy as np

class TestGrayscaleConversion(unittest.TestCase):
    
    def setUp(self):
        # Create a color image for testing
        self.color_img = Image.new("RGB", (100, 100), color="yellow")
        self.color_pixels = self.color_img.getdata()
        
        # Create a corresponding grayscale image for testing
        self.gray_img = Image.new("L", (100, 100), color=255)
        self.gray_pixels = np.array(self.gray_img).flatten()
    
    def test_conversion(self):
        # Convert the color image to grayscale
        gray_pixels = [int(0.21*r + 0.72*g + 0.07*b) for (r, g, b,) in self.color_pixels]
        
        # Check that the grayscale pixels match the expected values
        self.assertListEqual(list(gray_pixels), list(self.gray_pixels))
        
    def tearDown(self):
        # Delete the test images
        del self.color_img
        del self.gray_img
        del self.color_pixels
        del self.gray_pixels
        
if __name__ == "__main__":
    unittest.main()