def solution(order):
    stack = []
    answer = 0
    idx = 0

    for box in range(1, len(order) + 1):
        stack.append(box)

        while stack and stack[-1] == order[idx]:
            stack.pop()
            answer += 1
            idx += 1

            if idx == len(order):
                return answer

    return answer