import os
from PIL import Image
import sys

def is_image(filepath):
    try:
        img = Image.open(filepath)
        img.verify()
        return True
    except:
        return False
    
in_path=sys.argv[1].rstrip('/')
img_file_list=os.listdir(in_path)

for i in img_file_list:
    if is_image(in_path+'/'+i):
        imgID = '.'.join(i.split('.')[:-1])
        suffix = i.split('.')[-1]
        if imgID.endswith("small"):
            continue
        img=Image.open(in_path+'/'+i)
        if(img.size[0]>896):
            width = 896
            height = int(896*img.size[1]/img.size[0])
            img=img.resize((width,height))
        img.save("{imgPath}/{imgID}_small.{suffix}".format(imgPath = in_path, imgID = imgID, suffix = suffix))