from cv2 import *

capturedVideo = VideoCapture(0)

# Create the haar cascade
faceCascade = CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
	# Capture frame-by-frame
	temp, frame = capturedVideo.read()

	# Our operations on the frame come here
	gray = cvtColor(frame, COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
	)

	# verifies that the use is in fact, sus
	print("Sussy baka" if len(faces) >= 1 else " ")

	# Draw a rectangle around the faces
	for (x, y, width, height in faces:
		rectangle(frame, (x, y), (x+width, y+height), (0, 255, 0), 2)


	# Display the resulting frame
	imshow('frame', frame)
	if waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
capturedVideo.release()
destroyAllWindows()
