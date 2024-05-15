import os
import shutil



# source = 'text1.txt'
# destination_dir = '/Users/kofiarcher/Desktop/folder'
# destination_file = os.path.join(destination_dir, os.path.basename(source))

# try:
#     if os.path.exists(destination_file):
#         print('File already exists')
#     else:
#         shutil.move(source, destination_dir)
#         print(source, 'was moved')
# except FileNotFoundError:
#     print(source+ ' was not found')

# import os

file_to_remove = '/path/to/file.txt' 

try:
    if os.path.exists(file_to_remove):
        os.remove(file_to_remove)
        #os.rmdir
        # shutil.rmtree
        print(file_to_remove, 'was removed')
    else:
        print(file_to_remove, 'was not found')
except OSError as e:
    print('Error removing file:', e)