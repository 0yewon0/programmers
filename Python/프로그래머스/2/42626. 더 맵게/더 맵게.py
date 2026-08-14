import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while len(scoville) >= 2 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new_food = first + second * 2
        heapq.heappush(scoville, new_food)
        
        answer += 1
    
    if scoville[0] >= K:
        return answer
    
    return -1