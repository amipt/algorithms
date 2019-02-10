class Stack:
    list=[]
    def __init__(self):
        self.list = []
    def push(self,itm):
        self.list.insert(0,itm)
        return self.list
    def pop(self):
        itm  = self.list[0]
        del self.list[0]
        return itm
    def top(self):
        return self.list[0]
    def size(self):
        return len(self.list)
    def isEmpty(self):
        return len(self.list)==0