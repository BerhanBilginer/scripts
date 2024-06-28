import os 

file_path = "/media/berhan/Berhan/28-07-jetsondan-gelenler/dataset/"

count0 = 0 #bu boş durak sayısı
count1 = 0
#count2 = 0
#count3=0
#count4= 0


files_count = 0
classes = []
deneme = []
indis = []
count = 1

file_path0 = file_path+str(count)+'\\'

for files in os.listdir(file_path):
    #print(files)

    os.chdir(file_path)

    if files.endswith(".txt"):
        files_count +=1
        f = open(file=files)
        classes =  f.readlines()

        deneme = classes

        for i in range(0, len(classes)):
            print("indisler = ",deneme[i])
            indis = deneme[i]
            print("ilk indis = ",indis[0])
            if indis[0] == str(0):
                count0 +=1 
            elif indis[0] == str(1):
                count1 +=1 
            #elif indis[0] == str(2):
             #   count2 +=1 
            #elif indis[0] == str(2):
             #   count3 +=1 
            #elif indis[0] == str(2):
                #count4 +=1 


print("yelekli = ", count0)
print("yeleksiz = ", count1)
#print("cukur = ", count2)
#print("catlak = ", count2)
#print("calismiyor = ", count2)
print("toplam txt dosyasi = ", files_count)
print("toplam etiket dosyasi = ", count0+count1)