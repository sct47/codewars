def lettervalues(str):

    myList = list(str)
    ltrvalues = []
    for letter in myList:
        value = (ord(letter) - 96)
        ltrvalues.append(value)
    return ltrvalues
        
    # value = (ord(letter) - 96)
    # return value

print(lettervalues('seven'))


