import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
        
    def enqueue(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
        
    def dequeue(self):
        return heapq.heappop(self.elements)[1]
        
    def is_empty(self):
        return self.elements == []
        
    def size(self):
        return len(self.elements)
        
def main():
    pq = PriorityQueue()
    pq.enqueue(3, 3)
    pq.enqueue(2, 2)
    pq.enqueue(10, 1)
    pq.enqueue(4, 4)
    pq.enqueue(5, 5)
    print(pq.size())
    while not pq.is_empty():
        print(pq.dequeue())
    print(pq.size())
    
if __name__ == '__main__':
    main()
