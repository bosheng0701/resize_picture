from cv2 import resize,imread,imwrite,INTER_AREA
from os import path,mkdir,listdir
def read_directory(directory_name,resize_x,resize_y):
    for filename in listdir(r"./"+directory_name):
        img = imread(directory_name + "/" + filename)
        img= resize(img,(resize_x,resize_y),interpolation =INTER_AREA)
        filelocation='Resize_picture/'+filename
        imwrite(filelocation,img)
if not path.exists('./Resize_picture'):
    mkdir('Resize_picture')
directory_name=input('資料夾名稱: ')
resize_x=int(input('寬度: '))
resize_y=int(input('長度: '))
read_directory(directory_name,resize_x,resize_y)
