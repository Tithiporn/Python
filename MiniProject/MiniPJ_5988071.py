import cv2
import numpy as np
img = cv2.imread('C:/Users/USER/Desktop/Minion.jpg',1)
img2 = cv2.imread('C:/Users/USER/Desktop/Minion.jpg',1)
img =cv2.resize(img,(1080,1080))

#Category A
twocolorGR = img[0:360,0:360]
twocolorGR[:,:,0] = 0

onecolorB = img.copy()
topmed_onecolorB = img[0:360,360:720]
topmed_onecolorB[:,:,0] = 0
topmed_onecolorB[:,:,1] = 0

topright_twocolorBR = img[0:360,720:1080]
topright_twocolorBR[:,:,1] = 0

#Category B
img[360:720,0:360] =255-img[360:720,0:360]
weight = 150
brighter = np.ones(img.shape,dtype='uint8')
for i in np.arange(0,3):
    brighter[:, :, i] = cv2.add(img[:, :, i], weight)
    img[360:720,0:360] = cv2.add(img[360:720,0:360], weight)
    weight = 3

mm_highercontrast = cv2.multiply(img[360:720,360:720], weight)
img[360:720,360:720] = cv2.multiply(img[360:720,360:720], weight)

mr_lowercontrast = cv2.divide(img[360:720,720:1080], weight)
img[360:720,720:1080] = cv2.divide(img[360:720,720:1080], weight)


#Category C
butm_sobeledgeH = cv2.Sobel(img[720:1080,0:360], -1, 1, 0, ksize=3)
img[720:1080,0:360]=cv2.Sobel(img[720:1080,0:360], -1, 1, 0, ksize=3)

butm_sobeledgeV = cv2.Sobel(img[720:1080,360:720], -1, 0, 1, ksize=3)
img[720:1080,360:720]=cv2.Sobel(img[720:1080,360:720], -1, 0, 1, ksize=3)

def saltpepper_noise(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = np.random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

buttomright_saltpepper = saltpepper_noise(img[720:1080,720:1080],.03)
img[720:1080,720:1080] = saltpepper_noise(img[720:1080,720:1080],.03)

#showIMG = np.vstack((np.hstack((topleft_grayscale,topmed_onecolorB,topright_twocolorBR)), np.hstack((brighter, mm_highercontrast,mr_lowercontrast)), np.hstack((butm_sobeledgeH,butm_sobeledgeV,buttomright_saltpepper))))
cv2.imshow('Image',img)
#cv2.imshow('show',showIMG)
cv2.waitKey(0)
cv2.destroyAllWindows()