class MyQueue:

    def __init__(self):
        self.d= deque()

    def push(self, x: int) -> None:
        self.d.appendleft(x)

    def pop(self) -> int:
        return self.d.pop()
    def peek(self) -> int:
        return self.d[-1]

    def empty(self) -> bool:
        return len(self.d)==0
