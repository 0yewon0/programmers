def solution(sequence):
    pulse1 = []
    pulse2 = []
    
    for i in range(len(sequence)):
        if i % 2 == 0:
            pulse1.append(sequence[i])
            pulse2.append(-sequence[i])
        else:
            pulse1.append(-sequence[i])
            pulse2.append(sequence[i])
    
    def max_subarray(arr):
        current = arr[0]
        best = arr[0]
        
        for i in range(1, len(arr)):
            current = max(arr[i], current + arr[i])
            best = max(best, current)
        
        return best
    
    return max(max_subarray(pulse1), max_subarray(pulse2))