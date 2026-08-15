def solution(tickets):
    tickets.sort()
    visited = [False] * len(tickets)
    answer = []
    
    def dfs(now, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return True
        
        for i in range(len(tickets)):
            start, end = tickets[i]
            
            if not visited[i] and start == now:
                visited[i] = True
                
                if dfs(end, path + [end]):
                    return True
                
                visited[i] = False
        
        return False
    
    dfs("ICN", ["ICN"])
    
    return answer[0]