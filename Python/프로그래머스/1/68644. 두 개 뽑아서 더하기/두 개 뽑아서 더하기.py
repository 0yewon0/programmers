def solution(numbers):
    ans_set = set()
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!=j:
                ans_set.add(numbers[i]+numbers[j])
    
    answer = list(ans_set)
    answer.sort()
    return answer