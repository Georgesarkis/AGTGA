import cv2

def ActivityChecker(OldActivity, NewActivity):
    if(OldActivity == NewActivity):
        return True
    else:
        return False

def ViewChecker(img1,img2):
    value = cv2.subtract(img1, img2)
    if(value > 95):
        return True
    else:
        return False