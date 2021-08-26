
def result (text):
    countAlphaNum = 0
    for i in text:
        if i.isalnum ():                # check for alpha numeric values
            countAlphaNum += 1
    
    if countAlphaNum != 0:              # if there is any alpha numeric value, print 'true'
        print ("True")
    
    else:
        print ('False')
    
    countAlpha = 0
    for i in text:
        if i.isalpha ():                # check for alphabetic
            countAlpha += 1

    if countAlpha != 0:
        print("True")

    else:
        print('False')

    countDigit = 0
    for i in text:
        if i.isdigit():                 # check for digits
            countDigit += 1

    if countDigit != 0:
        print("True")

    else:
        print('False')

    countLower = 0
    for i in text:
        if i.islower():                 # check for lowercase values
            countLower += 1

    if countLower != 0:
        print("True")

    else:
        print('False')
            
    countUpper = 0
    for i in text:
        if i.isupper():                 # check for upper case values
            countUpper += 1

    if countUpper != 0:
        print("True")

    else:
        print('False')

string = input ()
result (string)
