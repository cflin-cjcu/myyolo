import os


allfiles = os.listdir('./abcd/train/')
for file in allfiles:
    if '.jpg' in file:
        print('abcd/train/'+file)