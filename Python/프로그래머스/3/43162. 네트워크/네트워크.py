def solution(n, computers):
    cnt = 0
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt+=1

    return cnt
