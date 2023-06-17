import functions as fs
import coloring as cl
from os.path import splitext
from sys import argv
from time import perf_counter
from prefab_arrays import PrefabArray
from viewer import TextViewer
from tkinter import Tk

_time = perf_counter()

def update_time(message, color):
    global _time
    new_time = perf_counter()
    print(f'{color}{message} in {(new_time-_time):.4f}s{cl.RESET}')
    _time = new_time

def main(args):
    if len(args) not in [3,4,5] or 'help' in args:
        fs.help_text()
        return
    file_path, width, height, *ascii_array = args
    image = fs.read_image(file_path)
    update_time('Image loaded', cl.GREEN)
    image_grayscale = fs.convert_to_grayscale(image)
    update_time('Image converted to grayscale', cl.GREEN)
    image_grayscale_resized = fs.resize_image(image_grayscale, (int(width), int(height)))
    update_time('Image resized', cl.GREEN)
    ascii_array = PrefabArray.get_array(ascii_array[0] if ascii_array else 'DETAILED')
    matrix_ascii = fs.convert_to_ascii(image_grayscale_resized, ascii_array)
    update_time('Image converted to ASCII', cl.GREEN)
    text = fs.matrix_to_text(matrix_ascii)

    result_file = f'{splitext(file_path)[0]}.txt'
    with open(result_file, 'w', encoding = 'utf-8') as f:
        f.write(text)

    print(f'{cl.BLUE}Done! Result was saved in file: {result_file}{cl.RESET}')

    print('Opening ASCII art in viewer')

    root = Tk()
    root.title("Text Viewer")
    root.geometry("800x600")
    viewer = TextViewer(root)

    viewer.set_text(text)

    viewer.set_font_size(1)

    root.mainloop()

if __name__ == '__main__':
    main(argv[1:])