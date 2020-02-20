import numpy as np
import cv2


def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()


blur_threshold=100
light_lower = 100
light_upper = 150
contr_threshold = 15

cap = cv2.VideoCapture(0) #cv2.VideoCapture('slow.flv')

while(1):
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    fm = variance_of_laplacian(frame_gray)
    blur_text = "Not Blurry"

    if fm < blur_threshold:
        blur_text = "Blurry"

    light_text = 'Good Lighting '
    mean, std = cv2.meanStdDev(frame_gray)
    mean = mean[0][0]
    std = std[0][0]
    if mean > light_upper:
        light_text = "Too Bright"
    elif mean < light_lower:
        light_text = 'Too Dark'

    contr_text = "Good Contrast"
    if std < contr_threshold:
      contr_text = "Poor Contrast"

    img = cv2.putText(frame, "{}: {:.2f}".format(blur_text, fm), (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    img = cv2.putText(img, "{}: {:.2f}".format(light_text, mean), (10, 60),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    img = cv2.putText(img, "{}: {:.2f}".format(contr_text, std), (10, 90),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow('frame',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()



