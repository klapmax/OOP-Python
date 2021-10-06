from sys import argv

userinp = argv[1:]

signs = "+-*/"

def answ(userinp):
    if len(userinp) == 3 and userinp[1] in signs:   
        try:
            return eval(''.join(userinp))   
        except:
            return None
    else:
        return None
print(answ(userinp))