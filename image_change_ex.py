from PIL import Image
import pytesseract
import os
import os.path as osp

path = r"/Users/Metatrons/Desktop/Python/test"
#得到文件夹下的所有文件名称
files_name = os.listdir(path)
# print(files_name)
# exit(0)
#print(files_name)
#exit(0)
def is_img(file):
    Group_Img = ['.jpg','.png','.jpeg']
    files = file.lower()
    if files in Group_Img:
        return True
    else:
        pass

i=0
for file in files_name:
    if is_img(osp.splitext(file)[1]):
        img = Image.open(file)
        pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
        text = pytesseract.image_to_string(img, lang='chi_tra')
        #print(text)
        i= i +1
        directory = "/Users/Metatrons/Desktop/Python/test/%s.txt" % file
        with open(directory,"w") as f:
            f.write(text) 
    else:
        pass
print(i)