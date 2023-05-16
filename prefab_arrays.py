from enum import Enum


class PrefabArray(Enum):
    DETAILED = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
    FULL = [' ', '.', '\'', '`', '^', '"', ',', ':', ';',
            'I', 'l', '!', 'i', '>', '<', '~', '+', '_',
            '-', '?', ']', '[', '}', '{', '1', ')', '(', 
            '|', '\\', '/', 't', 'f', 'j', 'r', 'x', 'n',
            'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 
            'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q', 'p', 
            'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 
            'W', '&', '8', '%', 'B', '@', '$']
    GRAFFITI = ['#', '$', '%', '&', '+', '-', '*', '=', '@']
    PIXEL_ART = [' ', '.', ',', ':', ';', 'o', 'O', '*', '+']
    GEOMETRIC_SHAPES = [' ', '▫', '□', '▧', '▤', '▣', '▥', '▩', '▨', '▪', '■', '▦']
    GALACTIC = ['.', '*', '•', '⚫', '⬤', '●', '◆', '◇', '○', '◌', '⦾', '⦿']
    FUTURISTIC = ['▪', '▫', '◻', '◼', '□', '■', '▣', '▣', '▤', '▥', '▦', '▧']
    PIXELATED = [' ', '░', '▒', '▓', '█']
    NATURE = [' ', '.', ',', ':', ';', '¤', '♠', '♣', '♥']
    GRAIL = ['#', '%', '+', '=', '*', ':', '.', ' ']
    SHADE = [' ', '░', '▒', '▓', '█']
    

    @classmethod
    def get_array(cls, name):
        return cls[name.upper()].value
    

    @classmethod
    def get_all(cls):
        return [array.name for array in PrefabArray]