class Queue:
    def __init__(self) -> None:
        self.arr = []
    def push(self, val):
        self.arr.append(val)
    def pop(self):
        return self.arr.pop(0)

class Stack:
    def __init__(self) -> None:
        self.arr = []
    def push(self, val):
        self.arr.append(val)
    def pop(self):
        return self.arr.pop(-1)

