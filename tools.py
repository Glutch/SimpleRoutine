import os
import ctypes
from PIL import Image
import pyautogui

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),("y", ctypes.c_long)]

# Gotta take a screenshot and count how wide every pixel is
PIXEL_SIZE_ON_SCREENSHOT = 3

# Hanterar så att terminalen refreshar fint
class WindowsConsoleOutput():
    STD_OUTPUT_HANDLE = -11

    def __init__(self):
        self.handle = ctypes.windll.kernel32.GetStdHandle(self.STD_OUTPUT_HANDLE)

    def write(self, x, y, text):
        ctypes.windll.kernel32.SetConsoleCursorPosition(self.handle, ctypes.wintypes._COORD(x, y))
        ctypes.windll.kernel32.WriteConsoleA(self.handle, text, 30, None, None)

console_out = WindowsConsoleOutput()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Gör om rgb till number
def rgb_to_number(rgb):
    if all(isinstance(val, int) for val in rgb):
        number = (rgb[0] << 16) + (rgb[1] << 8) + rgb[2]
    elif all(isinstance(val, float) for val in rgb):
        number = (rgb[0] / 255.0) + (rgb[1] / 255.0 / 256.0) + (rgb[2] / 255.0 / 256.0 / 256.0)
    else:
        raise TypeError("Unsupported RGB type. Only int and float lists are supported.")
    
    return number

# # Hämtar pixelns rgb
def get_pixel_color(x, y):
    hDC = ctypes.windll.user32.GetDC(0)
    RGB = ctypes.windll.gdi32.GetPixel(hDC, x, y)
    ctypes.windll.user32.ReleaseDC(0, hDC)
    red = RGB & 255
    green = (RGB >> 8) & 255
    blue = (RGB >> 16) & 255
    return [red, green, blue]

# Hämtar pixelns rgb, parsear, printar den till terminalen
def get_pixel(i, name):
    pixel_color = get_pixel_color((i - 1) * PIXEL_SIZE_ON_SCREENSHOT, 0)
    parsed_color = rgb_to_number(pixel_color)
    text = f"{name}: {parsed_color}" + (' ' * 10)
    console_out.write(0, i - 1, text)
    return parsed_color

def get_all_pixel():
    #WIP for later use
    count = get_pixel(1, "count")
    name = "test" 
    for pixels in range(1, count):
        get_pixel(pixels, name + str(pixels))
    


def press(button, modifier = None):
  if modifier:
    pyautogui.keyDown(modifier)

  pyautogui.press(button)

  if modifier:
    pyautogui.keyUp(modifier)