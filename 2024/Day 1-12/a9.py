def part_1(A):
    i = 0
    e = len(A)+1
    index = 0
    id1 = 0
    id2 = len(A)//2
    blist = []
    total = 0
    
    while i < e:
        size = int(A[i])
        for k in range(index, index+size):
            total += id1*k
        index += size
        id1 += 1
        
        ### Add from end
        size = int(A[i+1])
        while len(blist) < size:
            e -= 2
            blist.extend([id2 for x in range(int(A[e]))])
            id2 -= 1

        for k in range(index, index+size):
            elem = blist.pop(0)
            total += elem*k
        index += size
        i += 2
    
    while len(blist) > 0:
        elem = blist.pop(0)
        total += elem*index
        index += 1
    
    print(total)


def part_2(A):
    A = list(A)
    for i, size in enumerate(A):
        if i%2 == 0:
            A[i] = (int(size), i//2)
        else:
            A[i] = (int(size), -1)
    
    i = len(A)-1
    while i >= 0:
        if A[i][1] == -1: ### Free
            i -= 1
            continue
        bsize = A[i][0]
        for j, b in enumerate(A):
            if j >= i:
                break
            if b[0] >= bsize and b[1] == -1:
                if bsize != b[0]:
                    A.insert(j+1, (b[0]-bsize, -1))
                    i += 1
                A[j] = A[i]
                A[i] = (bsize, -1)
                break
        i -= 1
    
    ### Checksum
    i = 0
    c = 0
    for a in A:
        if a[1] != -1:
            for j in range(a[0]):
                c += a[1]*i
                i+=1
        else:
            i += a[0]
    print(c)

def main():
    A = []
    with open('2024/data/a9.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file][0]
    
    part_1(A)
    part_2(A)

if __name__ == '__main__':
    main()