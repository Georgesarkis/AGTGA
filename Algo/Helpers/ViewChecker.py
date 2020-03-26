import cv2
import numpy as np

def ActivityChecker(OldActivity, NewActivity):
    if(OldActivity == NewActivity):
        return True
    else:
        return False

def ViewChecker(img1,img2):
    image1 = cv2.imread(img1)
    image2 = cv2.imread(img2)
    return image1.shape == image2.shape and not (np.bitwise_xor(image1, image2).any())