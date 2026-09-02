import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    
    for _ in range(n):
        biggest = heapq.heappop(works)
        biggest += 1
        heapq.heappush(works, biggest)
    
    return sum(w ** 2 for w in works)