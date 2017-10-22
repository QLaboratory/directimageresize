import cv2
import os  
     
def file_name(file_dir):   
    image_name = list()
    for root, dirs, files in os.walk(file_dir):
        #print('hello')
        #print(root)  
        #print(files)
        image_name = files
    return image_name



#input file dir path
file_dir_path = '/home/yan/Desktop/scene_train_images_20170904/';
out_dir_path = '/home/yan/Desktop/direct_resize_folder/'

#get image
image_name = file_name(file_dir_path)

for image in image_name:
    print('process %d',image)
    image_file_path = file_dir_path+image 
    img=cv2.imread(image_file_path)
    res=cv2.resize(img,(32,32),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(out_dir_path+image,res);





