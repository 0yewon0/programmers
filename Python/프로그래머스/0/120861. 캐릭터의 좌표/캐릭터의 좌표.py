def solution(keyinput, board):
    x, y = 0, 0
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    for key in keyinput:
        if key == "left":
            if x > -max_x:
                x -= 1
        elif key == "right":
            if x < max_x:
                x += 1
        elif key == "up":
            if y < max_y:
                y += 1
        elif key == "down":
            if y > -max_y:
                y -= 1
    return [x, y]
