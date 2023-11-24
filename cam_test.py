#cam test

from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import os 	# so the script can automatically send the CSV file to dropbox

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
# 	help="path to output CSV file containing barcodes")
# args = vars(ap.parse_args())

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
# vs = VideoStream(src=0).start()   
cap = cv2.VideoCapture(1,cv2.CAP_V4L2)#VideoStream(usePiCamera=True).start() 
time.sleep(2.0)

cap.set(3,640)
cap.set(4,480)
cap.set(5,30)

# open the output CSV file for writing and initialize the set of
# barcodes found thus far
csv = open("barcode.csv","w")
found = set()

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it to
	# have a maximum width of 400 pixels
	ret,frame = cap.read()
	#frame = imutils.resize(frame, width=400)
    # vs.set(3,640)
    # vs.set(4,480)
    # vs.set(5,30)
    
 

	# find the barcodes in the frame and decode each of the barcodes
	barcodes = pyzbar.decode(frame)

	# loop over the detected barcodes
	for barcode in barcodes:
		# extract the bounding box location of the barcode and draw
		# the bounding box surrounding the barcode on the image
		(x, y, w, h) = barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

		# the barcode data is a bytes object so if we want to draw it
		# on our output image we need to convert it to a string first
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type

		# draw the barcode data and barcode type on the image
		text = "{} ({})".format(barcodeData, barcodeType)
		cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

		# if the barcode text is currently not in our CSV file, write
		# the timestamp + barcode to disk and update the set
		if barcodeData not in found:
			csv.write("{},{}\n".format(datetime.datetime.now(),
				barcodeData))
			csv.flush()
			found.add(barcodeData)
			

	# show the output frame
	cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
csv.close()
#cv2.destroyAllWindows()
cap.release()
cv2.destroyAllWindows()



# import cv2

# camera_id = 1
# delay = 1
# window_name = 'OpenCV Barcode'

# bd = cv2.barcode.BarcodeDetector()
# cap = cv2.VideoCapture(camera_id,cv2.CAP_V4L2)

# while True:
#     ret, frame = cap.read()

#     if ret:
#         ret_bc, decoded_info, _, points = bd.detectAndDecode(frame)
#         if ret_bc:
#             frame = cv2.polylines(frame, points.astype(int), True, (0, 255, 0), 3)
#             for s, p in zip(decoded_info, points):
#                 if s:
#                     print(s)
#                     frame = cv2.putText(frame, s, p[1].astype(int),
#                                         cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
#         cv2.imshow(window_name, frame)

#     if cv2.waitKey(delay) & 0xFF == ord('q'):
#         break

# cv2.destroyWindow(window_name)
