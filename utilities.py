# IP validator
import struct
import pickle
import os
import cv2
import socket
import hashlib
import time

from client_data import *

supportedObjects = ['person', 'bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant',
	'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 
	'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard',
	'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 
	'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'sofa', 'pottedplant', 'bed', 'diningtable', 'toilet', 'tvmonitor',
	'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase',
	'scissors', 'teddy bear', 'hair drier', 'toothbrush']

def validateIP(IP):
	if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
		return True
	return False


def isIPv4(s):
	try: return str(int(s)) == s and 0 <= int(s) <= 255
	except: return False

# Port validator


def validatePort(port):
	try: return str(int(port)) == port and 0 <= int(port) <= 65535
	except: return False

# Navigation Inputs validator


def validateNavInputs(valueDict):
	valueList = list(valueDict.values())
	for value in valueList:
		try:
			if(float(value) < 0): return False
		except: return False
	return True

# Mapping Inputs validator


def validateMappingInputs(valueDict):
	validationCheckList = [validateModelInput(valueDict["model"]), validateBubbleInput(valueDict["bubble"]), validateBlockResInput(
		valueDict["block"]), validatePointorCloudInputs(valueDict["point"]), validatePointorCloudInputs(valueDict["cloud"]), validateSlantInput(valueDict["slant"])]
	if False in validationCheckList:
		return False
	else:
		return True


def validateModelInput(value):
	try: return value == "" or (0 <= float(value) <= 1)
	except: return False


def validateBubbleInput(value):
	try: return value == "" or (str(int(value)) == value and 1 <= int(value) <= 10 and int(value) % 2 != 0)
	except: return False


def validateBlockResInput(value):
	try: return value == "" or (str(int(value)) == value and 32 <= int(value) <= 128)
	except: return False


def validatePointorCloudInputs(value):
	try: return value == "" or (str(int(value)) == value and 1 <= int(value) <= 100)
	except: return False


def validateSlantInput(value):
	try: return value == "" or (str(int(value)) == value and 0 <= int(value) <= 10)
	except: return False

import threading


class Yolo():

	def __init__(self, trainedModelRelativePath, confidence = 0.5, threshold = 0.3):
		# Parameters to be used
		self.confidenceValue = confidence
		self.thresholdValue = threshold

		# load the COCO class labels our YOLO model was trained on
		# yoloRelativePath = 'yolo-object-detection/yolo-coco'
		self.yoloAbsolutePath = os.path.join(os.getcwd(), trainedModelRelativePath)
		labelsPath = os.path.sep.join([self.yoloAbsolutePath, "coco.names"])
		self.LABELS = open(labelsPath).read().strip().split("\n")

		# initialize a list of colors to represent each possible class label
		np.random.seed(42)
		self.COLORS = np.random.randint(0, 255, size=(len(self.LABELS), 3), dtype="uint8")

		# derive the paths to the YOLO weights and model configuration
		weightsPath = os.path.sep.join([self.yoloAbsolutePath, "yolov3.weights"])
		configPath = os.path.sep.join([self.yoloAbsolutePath, "yolov3.cfg"])

		# load our YOLO object detector trained on COCO dataset (80 classes)
		print("[INFO] loading YOLO from disk...")
		self.net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

		# determine only the *output* layer names that we need from YOLO
		self.ln = self.net.getLayerNames()
		self.ln = [self.ln[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

	def produceYoloImage(self,image):
		# load our input image and grab its spatial dimensions
		# image = cv2.imread(image) #image needs change
		(H, W) = image.shape[:2]

		# construct a blob from the input image and then perform a forward
		# pass of the YOLO object detector, giving us our bounding boxes and
		# associated probabilities
		blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
		self.net.setInput(blob)
		start = time.time()
		layerOutputs = self.net.forward(self.ln)
		end = time.time()

		# show timing information on YOLO
		# print("[INFO] YOLO took {:.6f} seconds".format(end - start))

		# initialize our lists of detected bounding boxes, confidences, and
		# class IDs, respectively
		boxes = []
		confidences = []
		classIDs = []

		# Return objects found list
		objectsFound = []

		# loop over each of the layer outputs
		for output in layerOutputs:
			# loop over each of the detections
			for detection in output:
				# extract the class ID and confidence (i.e., probability) of
				# the current object detection
				scores = detection[5:]
				classID = np.argmax(scores)
				confidence = scores[classID]

				# filter out weak predictions by ensuring the detected
				# probability is greater than the minimum probability
				if confidence > self.confidenceValue:
					# scale the bounding box coordinates back relative to the
					# size of the image, keeping in mind that YOLO actually
					# returns the center (x, y)-coordinates of the bounding
					# box followed by the boxes' width and height
					box = detection[0:4] * np.array([W, H, W, H])
					(centerX, centerY, width, height) = box.astype("int")

					# use the center (x, y)-coordinates to derive the top and
					# and left corner of the bounding box
					x = int(centerX - (width / 2))
					y = int(centerY - (height / 2))

					# update our list of bounding box coordinates, confidences,
					# and class IDs
					boxes.append([x, y, int(width), int(height)])
					confidences.append(float(confidence))
					classIDs.append(classID)

		# apply non-maxima suppression to suppress weak, overlapping bounding
		# boxes
		idxs = cv2.dnn.NMSBoxes(boxes, confidences, self.confidenceValue, self.thresholdValue)

		# ensure at least one detection exists
		if len(idxs) > 0:
			# loop over the indexes we are keeping
			for i in idxs.flatten():
				# extract the bounding box coordinates
				(x, y) = (boxes[i][0], boxes[i][1])
				(w, h) = (boxes[i][2], boxes[i][3])

				# draw a bounding box rectangle and label on the image
				color = [int(c) for c in self.COLORS[classIDs[i]]]
				cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
				text = "{}: {:.4f}".format(self.LABELS[classIDs[i]], confidences[i])
				objectsFound.append(self.LABELS[classIDs[i]])
				cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

		return {'image':image, 'objects':objectsFound}

def confirmIfObjFound(UIobj, objInNeed):
	print("UI: ", UIobj.text())
	print("obj wanted: ", objInNeed)
	while True:
		if objInNeed in supportedObjects:
			print("in supported objs")
			print(YoloFrameData.foundObjects)
			if objInNeed in YoloFrameData.foundObjects:
				print("in found objs")
				UIobj.setText("Found {}".format(objInNeed))
				UIobj.setStyleSheet("color:rgb(0,220,0);")
			else:
				UIobj.setText("Found")
				UIobj.setStyleSheet("color:rgb(220,0,0);")
		else:
			UIobj.setText("Invalid Object")
			UIobj.setStyleSheet("color:rgb(220,220,0);")
			break
		
		time.sleep(0.2)


			

def imageRecievingClient(self,ip, port,feedStatus,dataholder, processingDataHolder, returningImageHolder):
	# URL = "http://192.168.0.147:8000/stream.mjpg"
	# inputStream = cv2.VideoCapture(URL)

	# while True:
		# _ret, image = inputStream.read()

		# imageHash = hashlib.sha1(image).hexdigest()
		# ClientData.uiInformation.waitingFrames.append(WaitingFrame(image, imageHash))
		# dataholder.append(image)

		# if len(dataholder) > 20:
		#     del dataholder[0:10]

		# time.sleep(0.01)

	port = int(port)
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# please change the ip address to your netowrks ip address
	client_socket.connect((ip, port))
	data = b""
	payload_size = struct.calcsize("Q")
	yoloClass = Yolo('yolo-object-detection/yolo-coco')

	# while True:
	while True:
		while len(data) < payload_size:
			packet = client_socket.recv(4 * 1024)
			if not packet: break
			data += packet

		packed_msg_size = data[:payload_size]
		data = data[payload_size:]
		msg_size = struct.unpack("Q", packed_msg_size)[0]

		while len(data) < msg_size:
			data += client_socket.recv(4*1024)
		frame_data = data[:msg_size]
		data = data[msg_size:]
		frame = pickle.loads(frame_data)

		if ClientData.uiInformation.viewType == 1:
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			#threshold1 = high intensity gradient
			#threshold2 = low intensity gradient
			#apertureSize = 3 - 7 smooth and sharpening
			#L2gradient = equation, False
			edges = cv2.Canny(frame, threshold1=30, threshold2=100)
			dataholder.append(edges)
		elif ClientData.uiInformation.viewType == 0:
			dataholder.append(frame)
		elif ClientData.uiInformation.viewType == 2:
			yoloImage = yoloClass.produceYoloImage(frame)
			dataholder.append(yoloImage["image"])
			print(yoloImage["objects"])
			YoloFrameData.foundObjects = yoloImage["objects"]
		
		# if len(dataholder) > 20:
		#     dataholder = dataholder[10:]

		# if len(processingDataHolder) > 10:
		#     dataForReducer = processingDataHolder[:10]
		#     processingDataHolder = processingDataHolder[10:]
		#     reduceThread = threading.Thread(target=encapsFrameReducer, args=(dataForReducer,5,returningImageHolder), daemon=True)
		#     reduceThread.start()

	client_socket.close()


def encapsFrameReducer(images, returnNum, resultHolder):
	# from reducer_class import Reducer
	# reducerClass = Reducer(imagesList, 5)
	# resultHolder = reducerClass.get_images()
	pass


def sendDataThroughSocket(IP, Port, cmd,args):
	Port = int(Port)
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((IP, Port))
		data_string = pickle.dumps({'command':cmd,'args':args}, protocol=2)
		s.send(data_string)
		data = s.recv(1024)
		if data:
			data = pickle.loads(data)
			return data['success']

'''
done and checked with this server in mind
import socket

HOST = '127.0.0.1'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	while True:
		s.listen()
		conn, addr = s.accept()
		print('Connected by', addr)
		data = conn.recv(32)
		if not data:
			pass
		print(data.decode('utf-8'))
'''

def recieveDisplayInformationDataSocket(UI, IP, Port, dataholder):
	Port = int(Port)
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((IP, Port))
		while True:
			s.listen()
			conn, addr = s.accept()
			print('Connected by', addr)
			data = conn.recv(4096)
			if not data:
				pass
			fetchedInformation = pickle.loads(data)
			dataholder.append(fetchedInformation)
			assignValues(UI, fetchedInformation)
'''
done and checked with this client in mind
import socket, pickle

informationDict = {"time": 45, "travel": "distance", "total distance": 45}


HOST = '127.0.0.1'
PORT = 8080
# Create a socket connection.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	data_string = pickle.dumps(informationDict)
	s.send(data_string)

print('Data Sent to Server')
'''

def assignValues(display, information):
	display.value_motion.setText(information["motion"])
	display.value_distance.setText(information["distance"])
	display.value_avg_speed.setText(information["avg_speed"])
	display.value_ultrasonic.setText(information["ultrasonic"])
	display.value_location.setText(information["location"])
	display.value_rotation.setText(information["rotation"])

if __name__ == "__main__":
	initiateYolo()
	print(ln)