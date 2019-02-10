class Queue:
    list = []
    def __init__(self):
        self.list = []
    def enQueue(self,itm):
        self.list.append(itm)
        return self.list
    def deQueue(self):
        return self.list.pop()
    