def solution(n, t, m, p):
    chars = "0123456789ABCDEF"
    
    def convert(num):
        if num == 0:
            return "0"
        
        result = ""
        
        while num > 0:
            result = chars[num % n] + result
            num //= n
        
        return result
    
    game = ""
    num = 0
    
    while len(game) < t * m:
        game += convert(num)
        num += 1
    
    answer = ""
    
    for i in range(t):
        answer += game[(p - 1) + i * m]
    
    return answer