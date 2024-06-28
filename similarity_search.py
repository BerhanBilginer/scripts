import numpy as np
import os
import cv2
import shutil

meanHistogram = []


def HistogramCalculator(src_img):

    while True:
        img = cv2.imread(src_img)
        label = cv2.selectROI("Label Selection",img,fromCenter=False)

        label_img = img[int(label[1]):int(label[1]+label[3]),
                        int(label[0]):int(label[0]+label[2])]

        gray_image = cv2.cvtColor(label_img,cv2.COLOR_BGR2GRAY)

        histogram = cv2.calcHist([gray_image], [0], None, [256], [0,256])

        mean_histogram = np.mean(histogram)
        meanHistogram.append(mean_histogram)

        print(f"Labeled Image Histogram is {mean_histogram}")

        if cv2.waitKey(1) == ord('q'):
            break

HistogramCalculator(src_img="/media/berhan/Berhan/28-07-jetsondan-gelenler/özgün/2023-07-27_16.56.15.930042.jpg")

def SimilaritySearcher(OtherImg,dst,threshold=0.2):

    kernel = (20,10)

    for others in os.listdir(OtherImg):
        os.chdir(OtherImg)
        if others.endswith(".jpg"):
                
            imagePath = os.path.join(OtherImg,others)
            otherImages = cv2.imread(imagePath)

            for y in range(0, (otherImages.shape[0] - kernel[0])):
                for x in range(0,(otherImages.shape[1]- kernel[1])):

                    region = otherImages[y:y+kernel[0],x:x+kernel[1]]

                    region_gray = cv2.cvtColor(region,cv2.COLOR_BGR2GRAY)
                    hist_region = cv2.calcHist([region_gray], [0], None, [256], [0, 256])
                    mean_hist_region = np.mean(hist_region)

                    if np.allclose(mean_hist_region, meanHistogram[0], atol=threshold):
                        shutil.copy(OtherImg+"/"+others,dst)
                        shutil.copy((OtherImg+"/"+others).replace(".jpg",".txt"),dst)

SimilaritySearcher(OtherImg="/media/berhan/Berhan/28-07-jetsondan-gelenler/deneme",dst="/media/berhan/Berhan/28-07-jetsondan-gelenler/deneme-dst")