paper = 0

with open("input1.txt") as f:
    for i in f.readlines():
        l, w, h = list(map(int, list(i.split('x'))))
        d1, d2, d3 = l * w, w * h, l * h
        m = min(d1, d2, d3)
        summ = (2 * d1 + 2 * d2 + 2 * d3) + m
        paper += summ


with open("output1.txt", "w") as f:
    print(paper, file=f)