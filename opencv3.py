import numpy as np
import cv2

from utils import  image_resize

cap = cv2.VideoCapture(0)

img_path = 'merve.jpg'
logo = cv2.imread(img_path, -1)
deneme = image_resize(logo, height= 100,width=100 )
deneme = cv2.cvtColor(deneme, cv2.COLOR_BGR2BGRA)



while 1:
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    frame_h, frame_w, frame_c = frame.shape
    # overlay with 4 channels BGR and Alpha
    overlay = np.zeros((frame_h, frame_w, 4), dtype='uint8')
    deneme_h, deneme_w, deneme_c = deneme.shape

    # replace overlay pixels with watermark pixel values
    for i in range(0, deneme_h):
        for j in range(0, deneme_w):
          #  if watermark[i,j][3] != 0:
                offset = 10
                h_offset = frame_h - deneme_h - offset
                w_offset = frame_w - deneme_w - offset
                overlay[i ,  offset +j] = deneme[i,j]

    cv2.addWeighted(overlay, 0.5, frame, 1.0, 0, frame)
    cv2.line(frame, (0, 100), (800, 100), (100, 0, 255), 2)
    cv2.rectangle(frame, (10, 450), (200, 300), (100, 0, 255), 1)
    # cv2.rectangle(frame, (630, 450), (400, 300), (100, 0, 255), 3)
    cv2.putText(frame, "1.TEST", (50, 380), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame, "2.TEST", (50, 430), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame, "MERVE", (500, 430), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.putText(frame, "TEST", (500, 80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)


    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()