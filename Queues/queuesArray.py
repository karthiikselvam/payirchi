class Queue:
    def __init__(self,limit = 10):
        self.limit = limit
        self.queue = []
        self.front = 0
        self.rear  = 0
        self.length = 0 

    def enque(self,item):
        if limit == length:
            print("Queue is Full")
        else:
            queue[rear] = item
            rear = (rear+1) % limit
            length += 1


    def deque(self, item):
        if length <= 0 :
            print("Queue is Empty")
        else:
            result = queue[front]
            front  = (front+1) % limit
            length -= 1


    
