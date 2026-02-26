def solution(brown, yellow):
    width = int(brown * 0.5) - 2
    height = 0
    while width >= height:
        if width * height == yellow:
            return [width + 2, height + 2]
        width -= 1
        height += 1