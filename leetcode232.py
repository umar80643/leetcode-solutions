class MyQueue:

    def __init__(self):
        self.queue = []


    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def peek(self) -> int:
        if len(self.queue) > 0:
            return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

myQueue = MyQueue();
myQueue.push(1);
myQueue.push(2);
myQueue.peek();
myQueue.pop();
myQueue.empty();
