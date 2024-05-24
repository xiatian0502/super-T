import shutil

# Specify the source file (the newly generated file)
source_file = '/path/to/new_mytvfree.m3u'

# Specify the destination file (the original file to be updated)
dest_file = '/path/to/mytvfree.m3u'

# Use the shutil module's copy function to overwrite the destination file with the source file
shutil.copy(source_file, dest_file)

print('File has been updated.')

