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
        print("Usage: ./convert.py [PATH_TO_FILE [FILE_01] [FILE_02] [FILE_03]] [FORMAT] [QUALITY (optional)]")
        quit()

def get_filename(img):
    img_name = img.filename.split('\\')[-1].split('/')[-1].split('.')[0]
    return img_name

def last_argument_is_quality():
    return sys.argv[-1].isdigit()

def get_type_to_convert():
    if(last_argument_is_quality()):
        return sys.argv[-2].lower()
    return sys.argv[-1].lower()

def get_files_to_convert():
    return sys.argv[1:-2] if last_argument_is_quality() else sys.argv[1:-1]

def get_quality():
    return int(sys.argv[-1]) if last_argument_is_quality() else 95

def convert(files):
    for file in files:
        img = Image.open(file)
        img.convert("RGB").save(f"{get_filename(img)} - Converted.{TYPE_TO_CONVERT}", TYPE_TO_CONVERT, optimize=True, quality=QUALITY)

check_params()

FILES_TO_CONVERT = get_files_to_convert()
TYPE_TO_CONVERT = get_type_to_convert() if get_type_to_convert() != 'jpg' else 'jpeg'
QUALITY = get_quality()
convert(FILES_TO_CONVERT)

if(len(FILES_TO_CONVERT) == 1):
    print(colorize("Image Converted!", 'yellow'))
else:
    print(colorize("Images Converted!", 'yellow'))