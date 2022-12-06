from Day06Input import *

def check_string(string):
    for n in string:
        # print(n)
        if string.count(n) > 1:
            return False
    return True

def check_signal(signal):
    for i in range(0,len(signal)-3):
        if check_string(signal[i:i+4]):
            return i+4

def check_message(signal):
    for i in range(0,len(signal)-3):
        if check_string(signal[i:i+14]):
            return i+14

print(check_signal(signal))
# Low (Probably by 1
#1080 - Yep!
print(check_message(signal))
# 3645
