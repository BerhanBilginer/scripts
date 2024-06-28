import os

img_path = 'E:\\Yogunluk_Data\\Datasets\\On_Kamera_Dataset\\'
count = 0

for img in os.listdir(img_path):
    print(img_path+img)
    print(img.split('.')[0])

    if img.endswith(".txt"):
        count+=1
        with open (img_path+img, 'r') as f:
            lines = f.readlines()
            
            
            if lines[0][0] == '0':
                with open(img_path+img.split('.')[0]+".txt", 'w') as txt:
                    txt.writelines("0 0.500244 0.500244 0.999512 0.999512") 
                txt.close()
            
            elif lines[0][0] == '1':
                with open(img_path+img.split('.')[0]+".txt", 'w') as txt:
                    txt.writelines("1 0.500244 0.500244 0.999512 0.999512") 
                txt.close()


            elif lines[0][0] == '2':
                with open(img_path+img.split('.')[0]+".txt", 'w') as txt:
                    txt.writelines("2 0.500244 0.500244 0.999512 0.999512") 
                txt.close()

            elif lines[0][0] == '3':
                with open(img_path+img.split('.')[0]+".txt", 'w') as txt:
                    txt.writelines("3 0.500244 0.500244 0.999512 0.999512") 
                txt.close()
            
            elif lines[0][0] == '4':
                with open(img_path+img.split('.')[0]+".txt", 'w') as txt:
                    txt.writelines("4 0.500244 0.500244 0.999512 0.999512") 
                txt.close()

print(count)