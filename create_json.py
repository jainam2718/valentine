import os
import json

def fetch_photos_json(fromyear, frommonth, toyear, tomonth):
    l = []
    for year in range(int(fromyear), int(toyear) + 1):
        start_month = int(frommonth) if year == int(fromyear) else 1
        end_month = int(tomonth) if year == int(toyear) else 12

        for month in range(start_month, end_month + 1):
            folder = f'./images/Valentine2k25/{year}_{str(month).zfill(2)}'
            if os.path.isdir(folder):
                images = [os.path.join(folder, img) for img in os.listdir(folder) if os.path.isfile(os.path.join(folder, img))]
                if images:
                    l.extend(images)
    return l

    with open(f'./json_files/{fromyear}_{frommonth}_{toyear}_{tomonth}.json', 'w') as json_file:
        json.dump(photos, json_file, indent=4)


x = [[2024, 6 , 2025, 2], [2024, 1, 2024, 5], [2023, 5 ,2023, 12], [2022, 9 ,2023, 4], [2022, 5, 2022, 8], [2018, 6, 2022, 4],
     [2016, 6, 2018, 5], [2014, 4, 2016, 5]]

photos = {}
for i, argu in enumerate(x):
    photos[i] = fetch_photos_json(*argu)

with open(f'./json_files/images.json', 'w') as json_file:
        json.dump(photos, json_file, indent=4)