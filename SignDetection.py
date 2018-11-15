import cv2			# openCV
import numpy as np #number library
import pyttsx # speech engine
import win32com.client # us this for windows | not needed in linux

#initialise the speech engine
engine = pyttsx.init()

### Load the XML files and declare them for use
stop_cascade = cv2.CascadeClassifier('stop.xml')
speedlimit_cascade = cv2.CascadeClassifier('speedlimit.xml')
lights_cascade = cv2.CascadeClassifier('lights.xml')
noentry_cascade = cv2.CascadeClassifier('noentry.xml')
school_cascade = cv2.CascadeClassifier('school.xml')
###
cap = cv2.VideoCapture(0)#### in () declare what camera you will use, 0 i.e. the laptops webcam
##start the loop
while True:
	ret, img = cap.read()	#retreive and read the camera
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert the retreived image to grayscale (easirer processing)
	#loops for each loaded xml file 
	stop = stop_cascade.detectMultiScale(gray, 1.3, 5) # detect on gray , image width and heigh
	for (x,y,w,h) in stop:
		cv2.rectangle (img, (x,y), (x+w, y+h), (255, 0,0), 2)	# start of the rectagle (x,y) , end of the rectagle (x+w, y+h), (color selection) in this case is blue, 2 is the line width
		roi_gray = gray[y:y+h, x:x+w]	# the region to look for in grayscale
		roi_color = img[y:y+h, x:x+w]	# the region in color
		print ("Found stop")			# Declare found 
		engine.say("Stop Sign")			# Announce it via the speech engine
		engine.runAndWait()				# Pause the engine

	speedlimit = speedlimit_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in speedlimit:
		cv2.rectangle (img, (x,y), (x+w, y+h), (255, 0,0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		print ("Found speedlimit")
		engine.say("Speed Limit is 50")
		engine.runAndWait()
		
	lights = lights_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in lights:
		cv2.rectangle (img, (x,y), (x+w, y+h), (255, 0,0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		print ("Found lights")
		engine.say("Traffic Lights Ahead")
		engine.runAndWait()

	noentry = noentry_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in noentry:
		cv2.rectangle (img, (x,y), (x+w, y+h), (255, 0,0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		print ("Found noentry")
		engine.say("No Entry")
		engine.runAndWait()

	school = school_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in school:
		cv2.rectangle (img, (x,y), (x+w, y+h), (255, 0,0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		print ("Found school")
		engine.say("School Ahead")
		engine.runAndWait()
		
	cv2.imshow('img', img)			# Show the image
	k = cv2.waitKey(30) & 0xff		# if "Esc" key is pushed break the loop
	if k == 27:
		break
		
cap.release()						# Stop capturing
cv2.destroyAllWindows()				# Close all windows
