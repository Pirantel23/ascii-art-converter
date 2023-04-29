from matplotlib.pyplot import imread
from PIL import Image
import numpy as np

ASCII_CHARACTERS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
ASCII_BASE = len(ASCII_CHARACTERS)
R_WEIGHT, G_WEIGHT, B_WEIGHT = 0.21, 0.72, 0.07


def help_text():
    print('''
To use this program run command like this:
python <script>.py <path_to_file>.png <width> <height> in python script
    or
ascii-converter.exe <path_to_file>.png <width> <height> in application
        ''')

def read_image(path: str):
    return imread(path)

def save_image(array, name):
    Image.fromarray(array).save(f"samples/{name}.png")

def convert_to_grayscale(image):
    height, width, channels = image.shape
    if channels < 3: return image # Image is already grayscale

    # Convert each pixel to grayscale
    # for y in range(height):
    #     for x in range(width):
    #         # Extract the R, G, and B components of the pixel
    #         pixel = image[y][x]
    #         r, g, b = pixel[:3]

    #         # Convert the pixel to grayscale using weighted sum of RGB values
    #         luminance = int(R_WEIGHT*r + G_WEIGHT*g + B_WEIGHT*b)

    #         # Set the pixel in the grayscale image array
    #         image[y][x] = luminance
    luminance = np.dot(image[...,:3], [0.21, 0.72, 0.07]).astype(np.uint8)

    return luminance

def resize_image(image, new_size):
    original_height, original_width = image.shape[:2]

    new_width, new_height = new_size

    resized_image = [[0 for _ in range(new_height)] for _ in range(new_width)]
    
    for y in range(new_width):
        for x in range(new_height):
            # Calculate coordinates of a pixel in original image
            orig_y = int(y * original_width / new_width)
            orig_x = int(x * original_height / new_height)

            orig_color = image[orig_x][orig_y]
            resized_image[y][x] = orig_color
    
    return resized_image

def convert_to_ascii(image, ascii_array):
    base = len(ascii_array)

    def get_ascii_character(luminance):
        return ascii_array[int(luminance/255*base)]
    
    result = []
    height, width = len(image), len(image[0])
    for y in range(width):
        line = []
        for x in range(height):
            line.append(get_ascii_character(image[x][y]))
        result.append(line)
    return result