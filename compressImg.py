import os,sys
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

def is_image(filepath):
    try:
        img = Image.open(filepath)
        img.verify()
        return True
    except:
        return False

h2p_compress_ratio = 2
in_path=sys.argv[1].rstrip('/')
img_file_list=os.listdir(in_path)

for i in img_file_list:
    if is_image(in_path+'/'+i):
        imgID = '.'.join(i.split('.')[:-1])
        suffix = i.split('.')[-1]
        if imgID.endswith("small"):
            continue
        if os.path.isfile(in_path+'/'+imgID+"_small."+suffix):
            continue
        img=Image.open(in_path+'/'+i)
        # if suffix.lower() == "heic":
        #     suffix = "png"
        #     img_raw=img.resize((int(img.size[0]/h2p_compress_ratio),int(img.size[1]/h2p_compress_ratio))).convert('sRGB')
        #     img_raw.save("{imgPath}/{imgID}.h2p.{suffix}".format(imgPath = in_path, imgID = imgID, suffix = suffix))
        if img.size[0]>img.size[1]:
            width = 896
        else:
            width =  448
        if(img.size[0]>width):
            height = int(width*img.size[1]/img.size[0])
            img=img.resize((width,height))#.convert('sRGB')

        img.save("{imgPath}/{imgID}_small.{suffix}".format(imgPath = in_path, imgID = imgID, suffix = suffix))
        # break