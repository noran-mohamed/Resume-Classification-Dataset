ERROR_MESSAGE = "Couldn't understand input. Please try again."
def takeInputFloat(message):
    while True:
        try:
            toReturn = float(input(message + ": "))
            break
        except:
            print(ERROR_MESSAGE)
            continue
    return toReturn

def takeInputInt(message):
    while True:
        try:
            toReturn = int(input(message + ": "))
            break
        except:
            print(ERROR_MESSAGE)
            continue
    return toReturn

def takeInputYesNo(message):
    while True:
        toReturn = input(message + "(y/n/yes/no): ")
        toTest = toReturn.lower()
        if toTest == "y" or toTest == "yes":
            return True
        if toTest == "n" or toTest == "no":
            return False
        else:
            print(ERROR_MESSAGE)
            continue

def takeInput(message):
    while True:
        toReturn = input(message + ": ")
        if toReturn.strip() == "":
            print(ERROR_MESSAGE + ". The input can't be empty")
            continue
        return toReturn