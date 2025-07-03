import cv2
import os
import re

# Doğru sıralama için özel sıralama fonksiyonu
def sorted_nicely(l):
    """ İnsan sırasına göre sıralama yapar. """
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)

# Görüntülerin bulunduğu klasör ve oluşturulacak video dosyasının yolu
image_folder = '/home/berhan/Desktop/zeg/area-violation/kuzeystar/results/pnm_iskele/2'
output_video = '/home/berhan/Desktop/zeg/area-violation/kuzeystar/results/pnm_iskele/2.mp4'

# Video fps değeri
frame_rate = 25

# Klasördeki .jpg dosyalarını al
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

# Dosyaları doğru sırada sıralayın
images = sorted_nicely(images)

# İlk görüntünün boyutunu alarak video boyutunu ayarla
img = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = img.shape

# Video dosyasını yazacak VideoWriter nesnesi
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec ayarlaması
out = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

# Tüm görüntüleri sırayla videoya ekleyin
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    out.write(frame)

# Video yazmayı bitir
out.release()

print(f"Video created: {output_video}")
