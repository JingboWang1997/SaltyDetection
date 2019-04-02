import cv2
import os
from PIL import Image

def renameAllFiles(dir, cls, format):
    for i, filename in enumerate(os.listdir(dir)): 
        dst = cls + '_' + str(i) + "." + format
        src = dir + filename 
        dst = dir + dst 
        os.rename(src, dst) 
    print('Finished')

def checkCorruptedImages(dir):
    corrupted = []
    for filename in os.listdir(dir):
        try:
            im=Image.open(dir + filename)
        except IOError:
            corrupted.append(filename)
    print('corrupted: ' + str(len(corrupted)))
    print(corrupted)
    return corrupted

renameAllFiles('salty food/', 'salty', 'jpg')
# checkCorruptedImages('salty food/')

