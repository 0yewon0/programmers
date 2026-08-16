import heapq

def solution(jobs):
    jobs.sort()  # 요청 시점 기준 정렬
    
    heap = []
    time = 0
    total = 0
    idx = 0
    count = 0
    
    while count < len(jobs):
        # 현재 시간까지 요청된 작업들을 힙에 넣기
        while idx < len(jobs) and jobs[idx][0] <= time:
            request, duration = jobs[idx]
            heapq.heappush(heap, (duration, request))
            idx += 1
        
        # 처리 가능한 작업이 있으면, 소요 시간이 가장 짧은 것부터 처리
        if heap:
            duration, request = heapq.heappop(heap)
            time += duration
            total += time - request
            count += 1
        
        # 처리 가능한 작업이 없으면, 다음 작업 요청 시간으로 이동
        else:
            time = jobs[idx][0]
    
    return total // len(jobs)