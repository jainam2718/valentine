import os

directory = "/Users/jainamshah2718/Desktop/valentine/images/Valentine2k25"  # Change this to the appropriate directory path
albums = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]

# Generate the HTML for the albums dynamically
html = '<ul>\n'
for idx, album in enumerate(albums, start=1):
    album_name = album.replace("_", " ").title()  # This could be adjusted to more neatly format album names
    html += f'  <li><a href="album.html?album={idx}">Album {idx}: {album_name}</a></li>\n'
html += '</ul>'

print(html)