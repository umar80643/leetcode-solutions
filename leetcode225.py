class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop(-1)

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


myStack = MyStack();
myStack.push(1);
myStack.push(2);
myStack.top();
myStack.pop();
myStack.empty();