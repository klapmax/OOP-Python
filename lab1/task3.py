import sys

sign = '+-'

def result(userInput, index, res):
    if not userInput[index].isdigit() and userInput[index] not in sign:
        return False, None
    elif userInput[index] in sign and index == len(userInput)-1:
        return False, None
    elif userInput[index] in sign and userInput[index+1] in sign:
        return False, None
    elif not userInput[index].isdigit() and userInput[index] not in sign:
        return False, None
    elif len(userInput)==0:
        return False, None 
    else:
        if index == len(userInput)-1:
            if len(userInput) == 1:
                return True, userInput[index]
            else:
                return True, res
        elif userInput[index] in sign:
            if not userInput[index+1].isdigit():
                return False, None
            if calculateNumber(userInput, index+1, '') != False:
                res = res + eval(userInput[index] + str(calculateNumber(userInput, index+1, '')))
                return result(userInput, index+1, res)
            else:
                return False,None
        elif index == 0:
            if userInput[index] not in sign:
                res += calculateNumber(userInput, index, '')
                return result(userInput, index+1, res)
            else:
                res = eval(userInput[index] +  str(calculateNumber(userInput, index+1, '')))
                return result(userInput, index+2, res)
        else:
            return result(userInput, index+1, res)

def calculateNumber(userInput, index, number):
    if userInput[index] not in sign and not userInput[index].isdigit():
        return False
    else:    
        if userInput[index] in sign:
            return eval(number)
        number += userInput[index]
        if index == len(userInput)-1:
            return eval(number)
    return calculateNumber(userInput, index+1, number)

if len(sys.argv)==1:
    print(False, None)
else:
    userInput = sys.argv[1]
    print(result(userInput, 0, 0))