def solution(n, k):
    converted = ""
    
    while n > 0:
        converted = str(n % k) + converted
        n //= k
    
    def is_prime(num):
        if num < 2:
            return False
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        
        return True
    
    answer = 0
    
    for x in converted.split("0"):
        if x and is_prime(int(x)):
            answer += 1
    
    return answer