class Test:
    __slots__ = 'left', 'right'

class Test2:
    def __init__(self):
        self.left = None
        self.right = None

a = Test()
b = Test2()

print(type(a.__slots__))
print(b.left)