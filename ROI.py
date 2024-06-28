"""
ROI ALGORITMASI 

1-) Videoyu ver
2-) videoyu istenen pixel degerlerine göre resize et
3-) videoyu resize ettikten sonra istenen araliklara göre böl
4-) bölünen her videoyu kaydet.

"""

import cv2

# Haar Cascade yüz sınıflandırıcısı yükleme
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mouth.xml')

# Girdi video dosyasını yükleme
cap = cv2.VideoCapture('input_video.mp4')

# Çıktı video dosyasını oluşturma
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, 20.0, (640, 360))

while True:
    # Girdi video dosyasından bir kare okuma
    ret, frame = cap.read()
    
    if not ret:
        break

    # Grayscale olarak dönüştürme
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Yüzleri algılama
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Her yüz için ağız bölgesini tanıma
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        mouths = mouth_cascade.detectMultiScale(roi_gray, 1.5, 5)
        
        # Her ağız bölgesi için kırpma işlemi yapma
        for (mx,my,mw,mh) in mouths:
            cropped = roi_color[my:my+mh, mx:mx+mw]
            
            # Kırpılmış görüntüyü çıktı video dosyasına yazma
            out.write(cropped)

    # Görüntüyü ekranda gösterme
    cv2.imshow('frame', frame)
    
    # 'q' tuşuna basıldığında döngüyü sonlandırma
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bellek temizleme
cap.release()
out.release()
cv2.destroyAllWindows()