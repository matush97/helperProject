# imports
import os
import shutil

# new folder with photos
try:
    if not os.path.exists('photo_data'):
        os.makedirs('photo_data')
except OSError:
    print('Error: Creating directory of data')

# constants
substring = "visible_spectrum"

entries = os.listdir('frames/')
print(entries)

index = 0
for entry in entries:
    entry_2 = os.listdir('frames/' + entry)
    entry_3 = os.listdir('frames/' + entry + '/' + entry_2[0] + '/')

    visible_spectrum_list = [i for i in entry_3 if substring in i]
    print(visible_spectrum_list)

    for photo in visible_spectrum_list:
        print(photo)
        photo_path = 'frames/' + entry + '/' + entry_2[0] + '/' + photo
        print(photo_path)

        name_destination = './photo_data/d' + str(index) + '.jpg'
        dest = shutil.move(photo_path, name_destination)

        index += 1
