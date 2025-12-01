mult = {'R':1, 'L':-1}

def p1(A):
    cval = 50
    zcnt = 0
    for a in A:
        d = mult[a[0]]*int(a[1:])
        cval = (cval+d)%100
        if cval == 0:
            zcnt += 1
    print(zcnt)


def p2(A):
    cval = 50
    zcnt = 0
    for a in A:
        d = mult[a[0]]*int(a[1:])
        zcnt -= cval == 0 and d < 0
        zval = (cval+d)//100
        cval = (cval+d)%100
        zcnt += abs(zval)
        zcnt += cval == 0 and d < 0
    print(zcnt)


def main():
    A = []
    with open('data/a1.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    p1(A)
    p2(A)
    

if __name__ == '__main__':
    main()