# Import libraries
import numpy
import cv2
import datetime
  
# open the video
vid = cv2.VideoCapture(0)
  
# Process untill end.
while(vid.isOpened()):
    ret, frame = vid.read()
    image = cv2.rotate(frame, cv2.cv2.ROTATE_180)
    if ret:
        # describe the type of 
        # font you want to display
        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
  
        # Get date and time and 
        # save it inside a variable
        dt = str(datetime.datetime.now())
  
        # put the dt variable over the
        # video frame
        frame = cv2.putText(image, dt,
                            (10, 100),
                            font, 1,
                            (210, 155, 155), 
                            4, cv2.LINE_8)
          
        # show the video
        cv2.imshow('frame', frame)
  
        key = cv2.waitKey(1)
          
        # define the key to
        # close the window
        if key == 'q' or key == 27:
            break
    else:
          
        break
          
          
# release the vid object
vid.release()
  
# close all the opened windows.
cv2.destroyAllWindows()