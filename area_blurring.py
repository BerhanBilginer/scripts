import cv2
import os

# Boş değişkenler
ref_points = []  # Birden fazla alanı tutmak için bir liste
cropping = False

# Fare olaylarını işlemek için bir fonksiyon
def click_and_crop(event, x, y, flags, param):
    global ref_points, cropping

    # Sol fare tuşuna basılırsa (Başlangıç noktası)
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_points.append([(x, y)])
        cropping = True

    # Sol fare tuşu bırakıldığında (Bitiş noktası)
    elif event == cv2.EVENT_LBUTTONUP:
        ref_points[-1].append((x, y))
        cropping = False

        # Dikdörtgen çiz
        cv2.rectangle(image, ref_points[-1][0], ref_points[-1][1], (0, 255, 0), 2)
        cv2.imshow("image", image)

# Görüntüyü yükleyin
input_image_path = '/home/berhan/Desktop/tersane/ui/2/UI_test_video329.jpg'  # Buraya kendi görüntü yolunuzu koyabilirsiniz
image = cv2.imread(input_image_path)
clone = image.copy()

# Girdinin ismi üzerine "_blurred" eklemek
file_name, file_extension = os.path.splitext(input_image_path)
output_image_path = f"{file_name}_blurred{file_extension}"

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    # 'r' tuşuna basarak görüntüyü sıfırlayın
    if key == ord("r"):
        image = clone.copy()
        ref_points = []  # Seçilen alanları sıfırla

    # 'c' tuşuna basarak seçilen tüm alanları bulanıklaştırın ve kaydedin
    elif key == ord("c"):
        if len(ref_points) > 0:  # En az bir alan seçildiğinde devam et
            for ref_point in ref_points:
                x1, y1 = ref_point[0]
                x2, y2 = ref_point[1]

                # Koordinatları doğru sıralamak (negatif değerlerden kaçınmak için)
                x1, x2 = min(x1, x2), max(x1, x2)
                y1, y2 = min(y1, y2), max(y1, y2)

                # Seçilen alanın koordinatları
                roi = clone[y1:y2, x1:x2]

                # Alanın boş olup olmadığını kontrol edin
                if roi.size > 0:
                    blurred_roi = cv2.GaussianBlur(roi, (51, 51), 0)
                    clone[y1:y2, x1:x2] = blurred_roi
                else:
                    print("Geçerli bir alan seçilmedi.")

            # Tüm alanlar bulanıklaştırıldıktan sonra kaydet ve göster
            cv2.imshow("Blurred Image", clone)
            cv2.imwrite(output_image_path, clone)
            print(f"Blurred image saved as {output_image_path}")
        else:
            print("Lütfen bir veya daha fazla alan seçin.")
        break

    # 'q' tuşuna basarak çıkın
    elif key == ord("q"):
        break

cv2.destroyAllWindows()
