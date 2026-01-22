# f = open("G:\\facultate\\anul 3 sem 1\\Retele neuronale\\proiect-Clasificator de piese\\data\\raw\\arbori\\arbori (1).jpg","rb")
# print(f.read())
# f.close()

# p = open("demo.txt")
# print(p.read(-10))
# p.close()

import os 
from os import listdir

folder_arbori = "G:\\facultate\\anul 3 sem 1\\Retele neuronale\\proiect-Clasificator de piese\\data\\raw\\arbori"
folder_bucse = "G:\\facultate\\anul 3 sem 1\\Retele neuronale\\proiect-Clasificator de piese\\data\\raw\\arbori"
folder_flanse = "G:\\facultate\\anul 3 sem 1\\Retele neuronale\\proiect-Clasificator de piese\\data\\raw\\arbori"

counter_img = 0;

# def preproces(simple_image):
#     return 



for images in os.listdir(folder_arbori):
    if(images.endswith(".jpg") or images.endswith('.webp') or images.endswith('.png') ):
        print(images)
        counter_img += 1
print(counter_img)
