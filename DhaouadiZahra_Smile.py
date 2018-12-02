#Dhaouadi Zohra Trace rectangle Recognition, simple version
#zohra.dhaouadi@esprit.tn
#Verion 3.7.1 latest version
#The Python Standard Library
#OpenCV library 3.4.1

#Biblio declaration
#import OpenCV module for binding and array conversion
import cv2
#Video display
#Change the path to 0 or your webcam number to make it work on your own camera
caption = cv2.VideoCapture("input.mp4")

#Cascade Classifier for Object Detection in a video stream
FC = cv2.CascadeClassifier("Face.xml")
#In case you want it to work on your local webcam you'll need to Change it to if(True) 
while(caption.isOpened()):
#Use one of the given Readers to read content into a CaptionSet object
	ret, frame = caption.read()


	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#detectMultiScale to perform the detection.
	faces = FC.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
	
	)

	print("I Found  your face SMILE =D , {0} faces! ".format(len(faces)))

	
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)



	cv2.imshow('Face', frame)
	#EXIT
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#Close all
caption.release()
cv2.destroyAllWindows()
