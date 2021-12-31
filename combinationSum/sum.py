def function_name(variable1, variable2):
    pass #code goes here

def isdivby3(x,y):
    pass #(x//3: >1)


def div3(x):
    return not x%3

def isdivby3(x):
    if x/3 == x//3:
        return True
    else:
        return False

print(div3(4),div3(3))
print(isdivby3(4), isdivby3(3))