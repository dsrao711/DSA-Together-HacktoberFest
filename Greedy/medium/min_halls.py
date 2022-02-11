import heapq

def solve():
    heap = []
    heapq.heappush(heap , (1))
    heapq.heappush(heap , (2))
    heapq.heappush(heap , (3))
    heapq.heappush(heap , (4))
    print(sorted(heap))
    
solve()