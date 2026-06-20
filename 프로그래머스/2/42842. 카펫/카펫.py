def solution(brown, yellow):
    # 2*w + 2*h - 4 = brown -> w + h = brown * 0.5 + 2
    # (w - 2) * (h - 2) == yellow
    # w * h == brown + yellow
    # w >= h
    total = int(brown*0.5) + 2
    for h in range(3, total):
        w = total - h
        if (w - 2) * (h - 2) == yellow:
            return [w, h]
    # width = int(brown * 0.5) - 2
    # height = 0
    # while width >= height:
    #     if width * height == yellow:
    #         return [width + 2, height + 2]
    #     width -= 1
    #     height += 1
    
    