# IP validator
import struct
import pickle
import cv2
import socket


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

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()
        self.status = False

    def stop(self):
        self._stop_event.set()
        self.status = False

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        while self.status:
            self.start()

def identify(dxnNum):
    if dxnNum == 8:
        return "up"
    elif dxnNum == 6:
        return "right"
    elif dxnNum == 2:
        return "down"
    elif dxnNum == 4:
        return "left"
    else:
        return "unknown"


def imageRecievingClient(ip, port,feedStatus,dataholder, processingDataHolder):
    port = int(port)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # please change the ip address to your netowrks ip address
    client_socket.connect((ip, port))
    data = b""
    payload_size = struct.calcsize("Q")

    while True:
    # while not self.stopped():
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
        myData = frame[-1][-1]
        # print(dataRepresentation)
        frame[-1][-1] = frame[-1][-2]
        dataRepresentation = {'frame':frame,'x':myData[0],'y':myData[1],'heading':identify(myData[2])} 
        processingDataHolder.append(dataRepresentation)
        # cv2.imshow("Received", frame)
        if feedStatus == "edge":
            print("in edge in util")
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #threshold1 = high intensity gradient
            #threshold2 = low intensity gradient
            #apertureSize = 3 - 7 smooth and sharpening
            #L2gradient = equation, False
            edges = cv2.Canny(frame, threshold1=30, threshold2=100)
            dataholder.append(edges)
        elif feedStatus == "raw":
            dataholder.append(frame)
        
        
        # if len(dataholder) > 20:
        #     dataholder = dataholder[10:]

        # if len(processingDataHolder) > 10:
        #     dataForReducer = processingDataHolder[:10]
        #     processingDataHolder = processingDataHolder[10:]
        #     reduceThread = threading.Thread(target=newimplemenationofreducedclass, args=(dataForReducer,5,returningImageHolder), daemon=True)
            #frameReducerCall
            # import frameReducer

            

    client_socket.close()


# sendData = {'up': 0, 'down': 0, 'right':0, 'left':0, 'frontdist':0, 'backdist':0, 'rightdist':0, 'leftdist':0}
def sendDataThroughSocket(IP, Port, cmd,args):
    Port = int(Port)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, Port))
        data_string = pickle.dumps({'command':cmd,'args':args})
        s.send(data_string)

def sendDataThroughSocketCheckSystem(IP, Port, cmd,args, returnVal):
    Port = int(Port)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, Port))
        data_string = pickle.dumps({'command':cmd,'args':args})
        s.send(data_string)
        recievedData = s.recv(1024)
        recievedData = recievedData.decode('utf-8')
        if recievedData == "pass":
            returnVal = 1
        else:
            returnVal = 0

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


# while True:
#     tryIP = input("Insert dict: ")
# a = {"model":"0","bubble":"1","block":"32","point":"1","cloud":"1","slant":"-1"}
# b = {"model":"0","bubble":"1","block":"32","point":"1","cloud":"1","slant":"0"}
# c = {"model":"0.1","bubble":"3","block":"78","point":"2","cloud":"1","slant":"1"}
# d = {"model":"0.5","bubble":"7","block":"127","point":"50","cloud":"1","slant":"11"}
# e = {"model":"1","bubble":"9","block":"128","point":"99","cloud":"1","slant":"9"}
# f = {"model":"1","bubble":"5","block":"128","point":"100","cloud":"100","slant":"10"}

# print("a - ", validateMappingInputs(a))
# print("b - ", validateMappingInputs(b))
# print("c - ", validateMappingInputs(c))
# print("d - ", validateMappingInputs(d))
# print("e - ", validateMappingInputs(e))
# print("f - ", validateMappingInputs(f))
# 49152 to 65535
