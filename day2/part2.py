summ = 0

with open("input2.txt") as f:
    for i in f.readlines():
        l, w, h = list(map(int, list(i.split('x'))))
        b = min(2 * l + 2 * h, 2 * w + 2 * h, 2 * l + 2 * w)
        w = l * w * h
        summ += (b + w)

with open("output2.txt", "w") as f:
    print(summ, file=f)