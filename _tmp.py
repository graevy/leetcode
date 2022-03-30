class Data:
    def __init__(self, arg_list, n=1):
        self.arg_list = arg_list
        self.n = n
        self.idx = 0
        self.max = len(arg_list)
    def get_args(self):
        out = self.arg_list[self.idx : self.idx + self.n]
        self.idx += self.n
        self.idx %= self.max
        return out


a = Data(['a','b','c','d','e','f'], n=2)
print(a.get_args())
print(a.get_args())
print(a.get_args())
print(a.get_args())

