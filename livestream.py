# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
def sketch(image):
 g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
 
 #to make the image edges more prominent 
 #we clean up the image using gaussian blur & smoothing 
 g_b=cv2.GaussianBlur(g,(5,5),0)
 
 #after that we apply canny edge detection
 c_e=cv2.Canny(g_b,40,80)
 
 #invert the binary image
 #mask is the net computed output
 #ret is the true or false stating that the command was executed
 #or not
 #ret,mask=cv2.threshold(c_e,70,255,cv2.THRESH_BINARY_INV)
 return c_e

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
 
 
	# show the frame
	cv2.imshow("Frame",sketch(image))
	key = cv2.waitKey(1)
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
camera.close()
cv2.destroyAllWindows()


