#!/usr/bin/env python
import cv2
import os
print("Package imported")


def import_video(video_mp4):
    # Video import
    cap = cv2.VideoCapture(video_mp4)
    # video is a series of images
    while True:
        success, img = cap.read()
        cv2.imgshow("Video", img)
        if cv2.waitkey(1) & 0xFF == ord('q'):
            # if q pressed, break out
            break

#def import_webcam():
    # webcam
    #cap = cv2.VideoCapture(0)  # webcam address - 0 is default
    #cap.set(3,640)  # width
    #cap.set(4,480)  # height
    #cap.set(10,100) #brightness


# Working with images - convert RGB img to grayscale
def convert_bgr_2_gray(color_filename, gray_filename):
    print(F"Converting {gray_filename} to grayscale")
    img_color = cv2.imread(color_filename)
    img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(gray_filename, img)
    return img

if __name__ == "__main__":
    print("Main")
    cv2.waitKey(0)
    img_gray = convert_bgr_2_gray("resources/lena.png", \
            "out/lena_gray.png")
    #cv2.imshow("gray", img_gray)
    
    
