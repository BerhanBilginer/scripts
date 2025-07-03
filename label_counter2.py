import os

file_path = "/home/berhan/Desktop/kiran/dataset/data/kiran_dataset_190325/dataset"
total_cls_count_list = []
empty_label_file_list = []
deleted_txt_files = []

for file in os.listdir(file_path):
    if file.endswith('.txt'):
        file_full_path = os.path.join(file_path, file)
        with open(file_full_path, 'r') as f:
            label = f.readlines()
            if label:
                for l in label: 
                    total_cls_count_list.append(l[0])
            else:
                empty_label_file_list.append(file)
                
                os.remove(file_full_path)
                deleted_txt_files.append(file)

cls_count = 4
total_cls_count = 0
for cls in range(cls_count):
    cls_count_for_cls = total_cls_count_list.count(str(cls))
    print(f'{cls} sınıfına ait: {cls_count_for_cls} adet etiketlenmiş veri bulunmaktadır.')
    total_cls_count += cls_count_for_cls

print('İçeriği boş olan etiket dosya isimleri:', empty_label_file_list)
print(f' {file_path} bulunan Toplam etiketli veri sayısı:', total_cls_count)

"""for txt_file in deleted_txt_files:
    jpg_file = os.path.join(file_path, txt_file.replace('.txt', '.jpg'))
    if os.path.exists(jpg_file):
        os.remove(jpg_file)
        print(f"Deleted corresponding jpg file: {jpg_file}")"""