import os

file_path = "/media/berhan/Berhan/UBUNTU/PPE/FIRE-DETECTION/D-Fire/train/labels/"
total_cls_count_list = []
empty_label_file_list = []

for file in os.listdir(file_path):
    if file.endswith('.txt'):
        with open(file_path + file, 'r') as f:
            label = f.readlines()
            if label:
                for l in label:
                    print(l)
                    total_cls_count_list.append(l[0])
                    print(l[0])
            else:
                print(file)
                empty_label_file_list.append(file)

cls_count = 2
cls = 0
total_cls_count = 0
print(len(total_cls_count_list))
for cls in range(cls_count):
    print(cls, 'sınıfına ait:', total_cls_count_list.count(str(cls)), 'adet etiketlenmiş veri bulunmaktadır.')
    total_cls_count =+ total_cls_count_list.count(str(cls))
print('İçeriği boş olan etiket dosya isimleri: ', empty_label_file_list)