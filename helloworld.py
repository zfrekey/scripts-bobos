import time
import string
text = "Ta lendo eh bixa"
temp = ""
for ch in text:
    for i in string.printable:
        if i == ch or ch == text:
            time.sleep(0.02)
            print(temp+i)
            temp += ch
            break
        else: 
            time.sleep(0.02)
            print(temp+i)
