#IP validator
def validateIP(IP):
    if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
        return True
    return False

def isIPv4(s):
    try: return str(int(s)) == s and 0 <= int(s) <= 255
    except: return False

#Port validator
def validatePort(port):
    try: return str(int(port)) == port and 0 <= int(port) <= 65535
    except: return False 

#Navigation Inputs validator
def validateNavInputs(valueDict):
    valueList = list(valueDict.values())
    for value in valueList:
        try: 
            if(float(value) < 0): return False
        except: return False
    return True

#Mapping Inputs validator
def validateMappingInputs(valueDict):
    validationCheckList = [validateModelInput(valueDict["model"]),validateBubbleInput(valueDict["bubble"]),validateBlockResInput(valueDict["block"]),validatePointorCloudInputs(valueDict["point"]),validatePointorCloudInputs(valueDict["cloud"]),validateSlantInput(valueDict["slant"])]
    if False in validationCheckList:
        return False
    else:
        return True
   

def validateModelInput(value):
    try: return value == "" or (0 <= float(value) <= 1)
    except: return False

def validateBubbleInput(value):
    try: return value == "" or (str(int(value)) == value and 1 <= int(value) <= 10 and int(value)%2 != 0)
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
#49152 to 65535