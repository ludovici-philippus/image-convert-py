from PIL import Image 
import sys

COLORS = {
    'RED': "\033[1;31m",
    'YELLOW': "\033[1;33m",
    'END': "\033[m",
}

def colorize(text, color):
    return f"{COLORS[color.upper()]}{text}{COLORS['END']}"

def check_params():
    if(len(sys.argv) < 3):
        print(colorize("[ERROR] You must use at least 2 params!", 'red'))
        print("Usage: ./convert.py [PATH_TO_FILE] [FORMAT] [QUALITY (optional)]")
        quit()

def get_filename(img):
    img_name = img.filename.split('\\')[-1].split('/')[-1].split('.')[0]
    return img_name

check_params()

BASE_FILE = sys.argv[1]
TYPE_TO_CONVERT = sys.argv[2].lower() if sys.argv[2].lower() != 'jpg' else 'jpeg'
QUALITY = int(sys.argv[3]) if len(sys.argv) > 3 else 95

img = Image.open(BASE_FILE)
img.convert("RGB").save(f"{get_filename(img)} - Converted.{TYPE_TO_CONVERT}", TYPE_TO_CONVERT, optimize=True, quality=QUALITY)
print(colorize("Image Converted!", 'yellow'))