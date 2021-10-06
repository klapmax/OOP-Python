from os import error
import sys 
import operator

def calc(str): 
    try:
        act = str[1]
        if act == 'add':return operator.add(int(str[2]), int(str[3]))
        elif act == 'mull':return operator.mull(int(str[2]), int(str[3]))
        elif act == 'divide':return operator.truediv(int(str[2]), int(str[3]))
        elif act == 'sub':return operator.sub(int(str[2]), int(str[3]))
    except:
        return None

print(calc(sys.argv[:]))