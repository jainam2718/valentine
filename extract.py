from PIL import Image
from datetime import datetime
from os import listdir, makedirs
from os.path import isfile, join, exists
import shutil
import re

def extract_date(path):
    
    image = Image.open(path)
    exifdata = image.getexif()
    print(exifdata)
    d = exifdata.get(306)
    if d:
        date_obj = datetime.strptime(d, "%Y:%m:%d %H:%M:%S")
        return date_obj.year, date_obj.month
    return None, None

def extract_date_from_filename(filename):
    # Check for any year between 2014 and 2025 in the filename
    year_pattern = re.compile(r'(201[4-9]|202[0-5])')
    match = year_pattern.search(filename)
    if match:
        year = int(match.group(0))
        # Extract the next two characters as the month
        month = None
        if len(filename) >= match.end() + 2:
            month_str = filename[match.end():match.end() + 2]
            if month_str.isdigit() and 1 <= int(month_str) <= 12:
                month = int(month_str)
        if month:
            return year, month
    return None, None

directory = "/Users/jainamshah2718/Desktop/valentine/images/Valentine2k25"

onlyfiles = [join(directory, f) for f in listdir(directory) if isfile(join(directory, f)) and f.lower().endswith('.jpg')]


for file in onlyfiles:
    year, month = extract_date_from_filename(file)
    if year and month:
        target_folder = join(directory, f"{year}_{month:02}")
        if not exists(target_folder):
            makedirs(target_folder)
        shutil.move(file, join(target_folder, file.split("/")[-1]))
    else:
        print(file)