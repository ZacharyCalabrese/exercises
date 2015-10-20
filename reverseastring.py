input = "onewaystring"

def reverseRecursive(y):
    if len(y) > 0:
        reverse(y[1:])
        print y[0],

def reverseSimple(y):
    print y[::-1]
