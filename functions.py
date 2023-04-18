from matplotlib.pyplot import imread
from PIL import Image

ASCII_CHARACTERS = r'''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.'''
ASCII_BASE = len(ASCII_CHARACTERS)

def help_text():
    print('To use this program run command like this:\npython <script>.py <path_to_file>.png <width> <height>')

def read_image(path: str):
    return imread(path)

def save_image(array, name):
    Image.fromarray(array).save(f"samples/{name}.png")

def convert_to_grayscale(image):
    height, width, _ = image.shape

    for y in range(width):
        for x in range(height):
            pixel = image[x][y]
            r, g, b = pixel[:3] # Don't need alpha channel if it has one
            luminance = int(0.21*r + 0.72*g + 0.07*b) # Calculating luminance
            image[x][y] = luminance

    return image 

def resize_image(image, new_size):
    original_height, original_width, _ = image.shape

    new_width, new_height = new_size

    resized_image = [[0 for _ in range(new_height)] for _ in range(new_width)]
    
    for y in range(new_width):
        for x in range(new_height):
            # Calculate coordinates of a pixel in original image
            orig_y = int(y * original_width / new_width)
            orig_x = int(x * original_height / new_height)

            orig_color = image[orig_x][orig_y][0]
            resized_image[y][x] = orig_color
    
    return resized_image

def convert_to_ascii(array):
    result = []
    height, width = len(array), len(array[0])
    for y in range(width):
        line = []
        for x in range(height):
            line.append(get_ascii_character(array[x][y]))
        result.append(line)
    return result

def get_ascii_character(luminance):
    return ASCII_CHARACTERS[int(luminance/255*ASCII_BASE)]