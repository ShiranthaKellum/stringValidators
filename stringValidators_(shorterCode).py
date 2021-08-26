
def result (string):
    print (any ([i.isalnum () for i in string]))        # any method body returns a booleon value (true or false)
    print (any ([i.isalpha () for i in string]))
    print (any ([i.isdigit () for i in string]))
    print (any ([i.islower () for i in string]))
    print (any ([i.isupper () for i in string]))
        

string = input ()

result (string)