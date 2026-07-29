class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.front = 0
        self.rear = -1
        self.queue = [0] * k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front -1 ) % self.k
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.rear = 0
            self.front = 0
        else:
            self.rear = (self.rear +1) % self.k

        self.queue[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        else:
            self.front = (self.front + 1) % self.k
        self.size -=1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.rear = (self.rear - 1) % self.k
        self.size -=1
        return True


    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k




myCircularDeque = MyCircularDeque(3);
myCircularDeque.insertLast(1);
myCircularDeque.insertLast(2);
myCircularDeque.insertFront(3);
myCircularDeque.insertFront(4);
myCircularDeque.getRear();
myCircularDeque.isFull();
myCircularDeque.deleteLast();
myCircularDeque.insertFront(4);
print(myCircularDeque.getFront());

