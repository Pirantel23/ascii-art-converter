try:
    from matplotlib.pyplot import imread, imsave
except ModuleNotFoundError:
    import pip
    pip.main(['install','--quiet','numpy'])
    pip.main(['install','--quiet','matplotlib'])
    from matplotlib.pyplot import imread, imsave

from prefab_arrays import PrefabArray
ASCII_CHARACTERS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
ASCII_BASE = len(ASCII_CHARACTERS)
WEIGHTS = 0.21, 0.72, 0.07


def help_text():
    print('''
To use this program run command like this:
python <script>.py <path_to_file>.png <width> <height> <ascii_array_name>
Here's all the names of ascii arrays available:''')
    print(', '.join(PrefabArray.get_all()))


def read_image(path: str):
    return imread(path)[...,:3] * 255


def save_image(image, name):
    imsave(f"samples/{name}.png", image, cmap='gray')


def convert_to_grayscale(image):
    return [[int(sum(pixel * weight for pixel, weight in zip(row[x], WEIGHTS))) for x in range(len(row))] for row in image]


def resize_image(image, new_size):
    original_height, original_width = len(image), len(image[0])

    new_width, new_height = new_size

    resized_image = [[0 for _ in range(new_width)] for _ in range(new_height)]
    
    y_scale = original_width / new_width
    x_scale = original_height / new_height

    for y in range(new_width):
        for x in range(new_height):
            # Calculate coordinates of a pixel in original image
            orig_y = int(y * y_scale)
            orig_x = int(x * x_scale)

            try:
                resized_image[x][y] = image[orig_x][orig_y]
            except ValueError:
                resized_image[x][y] = image[orig_x][orig_y][0]
    
    return resized_image


def convert_to_ascii(image, ascii_array = PrefabArray.get_array('detailed')):
    base = len(ascii_array)

    def get_ascii_character(luminance):
        return ascii_array[int(luminance/255*base)]
    
    result = []
    width, height = len(image), len(image[0])
    for x in range(width):
        line = []
        for y in range(height):
            line.append(get_ascii_character(image[x][y]))
        result.append(line)
    return result


def matrix_to_text(matrix):
    return '\n'.join(map(''.join, matrix))