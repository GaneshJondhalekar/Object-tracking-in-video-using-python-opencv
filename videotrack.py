import cv2 as cv
import numpy as np



def nothing(self):
    pass

cv.namedWindow("Tracking_window")
cv.createTrackbar("LH","Tracking_window",0,255,nothing)
cv.createTrackbar("LS","Tracking_window",0,255,nothing)
cv.createTrackbar("LV","Tracking_window",0,255,nothing)

cv.createTrackbar("UH","Tracking_window",255,255,nothing)
cv.createTrackbar("US","Tracking_window",255,255,nothing)
cv.createTrackbar("UV","Tracking_window",255,255,nothing)
#cap=cv.VideoCapture(0)
cap=cv.VideoCapture("How_to_Time_Travel.mp4")
while cap.isOpened():
   
    r,img=cap.read()
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

    #Lower h,s,v values track from tracking window
    l_h=cv.getTrackbarPos("LH","Tracking_window")
    l_s = cv.getTrackbarPos("LS", "Tracking_window")
    l_v = cv.getTrackbarPos("LV", "Tracking_window")

    # Upper h,s,v values track from tracking window
    u_h = cv.getTrackbarPos("UH", "Tracking_window")
    u_s = cv.getTrackbarPos("US", "Tracking_window")
    u_v = cv.getTrackbarPos("UV", "Tracking_window")

    #Upperbound and lower bound of pixel of a color
    lb=np.array([l_h,l_s,l_v])
    ub = np.array([u_h,u_s,u_v])


    mask=cv.inRange(hsv,lb,ub)
    res=cv.bitwise_and(img,img,mask=mask)

    cv.imshow("mask",mask)
    cv.imshow("res", res)
    cv.imshow("img", img)
    cv.imshow("hsv", hsv)

    key=cv.waitKey(1)
    if key==27:
        break
cap.release()
cv.destroyAllWindows()
