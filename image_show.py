import cv2 

img = cv2.imread('images/invoice-sample.jpg')

while(True):
	cv2.imshow('invoice', img)
	if(cv2.waitKey(1) & 0xFF == 27):
		break
	

cv2.destroyAllWindows()
