
class minHeap:
    def __init__(self) -> None:
        self.heap = [0] #initialize with dummy element

    def print_heap(self):
        print(self.heap)


    def push(self, element:int) -> None:
        #push it to child right now
        self.heap.append(element)

        #get child index
        child = len(self.heap)-1
        #check the parent as parent<child
        parent = child//2

        while (self.heap[parent]>self.heap[child] and parent != 0):
            #lets swap
            self.heap[parent],self.heap[child] = self.heap[child],self.heap[parent]

            #then we propogate up
            #we make the child == parent
            #then we do parent = parent//2

            child = parent
            parent = parent//2


my_heap = minHeap()
my_heap.push(1)
my_heap.push(2)
my_heap.push(6)
my_heap.push(4)
my_heap.push(1)
my_heap.push(2)
my_heap.push(6)
my_heap.push(4)
my_heap.push(-4)



my_heap.print_heap()



    