def solution(n, words):
    answer = []
    li = [words[0]]
           
    for i in range(1, len(words)):
        if words[i-1][-1] == words[i][0] and words[i] not in li:
            li.append(words[i])
        else:
            return [(i % n) + 1, (i // n) + 1]
    return [0,0]
