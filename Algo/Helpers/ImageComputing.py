from skimage.measure import compare_ssim
import cv2

def ImageComputing(img1,img2):
	imageA = cv2.imread(img1)
	imageB = cv2.imread(img2)
	grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
	grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
	(score, diff) = compare_ssim(grayA, grayB, full=True)
	return score * 100