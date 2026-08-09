import queue


class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0,val)



    def pushMiddle(self, val: int) -> None:
        mid = (len(self.queue)-1)//2
        self.queue.insert(mid,val)


    def pushBack(self, val: int) -> None:
        self.queue.append(val)


    def popFront(self) -> int:
        if self.queue:
            return self.queue.pop(0)
        return -1

    def popMiddle(self) -> int:
        if self.queue:
            mid = (len(self.queue)-1)//2
            return self.queue.pop(mid)
        return -1


    def popBack(self) -> int:
        if self.queue:
            return self.queue.pop()
        return -1



q = FrontMiddleBackQueue();
q.pushFront(1);
q.pushBack(2);
q.pushMiddle(3);
q.pushMiddle(4);
q.popFront();
q.popMiddle();
q.popMiddle();
q.popBack()
q.popFront();

