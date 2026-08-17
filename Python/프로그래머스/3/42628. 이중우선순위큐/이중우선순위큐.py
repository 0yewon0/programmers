def solution(operations):
    q = []
    
    for op in operations:
        command, num = op.split()
        num = int(num)
        
        if command == "I":
            q.append(num)
            q.sort()
        
        elif command == "D":
            if not q:
                continue
            
            if num == 1:
                q.pop()      # 최댓값 삭제
            else:
                q.pop(0)     # 최솟값 삭제
    
    if not q:
        return [0, 0]
    
    return [q[-1], q[0]]