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


def imageRecievingClient(ip, port, dataholder):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # please change the ip address to your netowrks ip address
    client_socket.connect((ip, port))
    data = b""
    payload_size = struct.calcsize("Q")

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
        # cv2.imshow("Received", frame)
        dataholder.append(frame)

    client_socket.close()


# sendData = {'up': 0, 'down': 0, 'right':0, 'left':0, 'frontdist':0, 'backdist':0, 'rightdist':0, 'leftdist':0}
def sendDataThroughSocket(IP, Port, cmd,args):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((IP, Port))
		data_string = pickle.dumps({'command':cmd,'args':args})
        s.send(data_string)
        
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
