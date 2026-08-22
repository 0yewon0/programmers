def solution(brown, yellow):
    total = brown + yellow
    
    for x in range(3, total + 1): 
        if total%x != 0:
            continue
        
        y = total // x 
        
        if (x-2)*(y-2) == yellow:
            return [x, y] if x >= y else [y, x]
        