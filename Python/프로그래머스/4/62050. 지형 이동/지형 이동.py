from collections import deque

def solution(land, height):
    n = len(land)
    area = [[-1] * n for _ in range(n)]
    area_id = 0
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    def bfs(x, y, area_id):
        q = deque()
        q.append((x, y))
        area[x][y] = area_id
        
        while q:
            x, y = q.popleft()
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if 0 <= nx < n and 0 <= ny < n:
                    if area[nx][ny] == -1:
                        if abs(land[x][y] - land[nx][ny]) <= height:
                            area[nx][ny] = area_id
                            q.append((nx, ny))
    
    # 1. 사다리 없이 갈 수 있는 구역 나누기
    for i in range(n):
        for j in range(n):
            if area[i][j] == -1:
                bfs(i, j, area_id)
                area_id += 1
    
    # 구역이 하나뿐이면 사다리 필요 없음
    if area_id == 1:
        return 0
    
    # 2. 서로 다른 구역 사이의 간선 만들기
    edges = []
    
    for x in range(n):
        for y in range(n):
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if 0 <= nx < n and 0 <= ny < n:
                    a = area[x][y]
                    b = area[nx][ny]
                    
                    if a != b:
                        cost = abs(land[x][y] - land[nx][ny])
                        edges.append((cost, a, b))
    
    # 3. 크루스칼로 최소 비용 연결
    edges.sort()
    parent = [i for i in range(area_id)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        
        if root_a == root_b:
            return False
        
        parent[root_b] = root_a
        return True
    
    answer = 0
    
    for cost, a, b in edges:
        if union(a, b):
            answer += cost
    
    return answer