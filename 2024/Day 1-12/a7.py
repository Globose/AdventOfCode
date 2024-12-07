def eval(t1, t2, tot, i, cat):
    if i == len(t2):
        return tot == t1
    
    cat_scan = False
    if cat:
        cat_scan = eval(t1, t2, int(str(tot)+str(t2[i])), i+1, cat)
    return eval(t1, t2, tot*t2[i], i+1, cat) or eval(t1, t2, tot+t2[i], i+1, cat) or cat_scan


def main():
    A = []
    with open('2024/data/a7.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    
    xnt = 0
    B = []
    for l in A:
        nums = l.split()
        t1 = int(nums[0][:-1])
        t2 = [int(x) for x in nums[1:]]
        if eval(t1, t2, 0, 0, False):
            xnt += t1
        else:
            B.append((t1, t2))
    print(xnt)

    ### Part 2
    xt = 0
    for i, l in enumerate(B):
        if i%50 == 0:
            print("-", end='')
        if eval(l[0], l[1], 0, 0, True):
            xt += l[0]
    print(f"\n{xt+xnt}")


if __name__ == '__main__':
    main()
