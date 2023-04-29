import functions as fs
import coloring as cl
from os.path import splitext
from sys import argv
from time import perf_counter

_time = perf_counter()

def update_time(message, color):
    global _time
    new_time = perf_counter()
    print(f'{color}{message} in {(new_time-_time):.4f}s{cl.RESET}')
    _time = new_time

def main(args):
    if len(args) != 3 or '-help' in args:
        fs.help_text()
        return
    file_path, width, height = args
    image = (fs.read_image(file_path) * 255)
    update_time('Image loaded', cl.GREEN)
    image_grayscale = fs.convert_to_grayscale(image)
    update_time('Image converted to grayscale', cl.GREEN)
    image_grayscale_resized = fs.resize_image(image_grayscale, (int(width), int(height)))
    update_time('Image resized', cl.GREEN)
    matrix_ascii = fs.convert_to_ascii(image_grayscale_resized)
    update_time('Image converted to ASCII', cl.GREEN)
    text = '\n'.join(map(''.join, matrix_ascii))

    result_file = f'{splitext(file_path)[0]}.txt'
    with open(result_file, 'w') as f:
        f.write(text)

    print(f'{cl.BLUE}Done! Result was saved in file: {result_file}{cl.RESET}')

if __name__ == '__main__':
    main(argv[1:])