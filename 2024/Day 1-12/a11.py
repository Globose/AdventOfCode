def blink(d):
    if d == 0:
        return (1,)
    elif len(str(d))%2 == 0:
        ds = str(d)
        h1 = int(ds[:len(ds)//2])
        h2 = int(ds[len(ds)//2:])

        return (h1, h2)
    
    return (d*2024,)


def blink_r(d, depth, dset, lim):
    key = (d,depth)
    if key in dset:
        return dset.get(key)
    
    if depth >= lim:
        return 1
    
    size = 0
    for d2 in blink(d):
        tsize = blink_r(d2, depth+1, dset, lim)
        size += tsize

    dset[key] = size
    return size


def get_score(A, lim):
    dset = {}
    total = 0

    for a in A:
        total += blink_r(a, 0, dset, lim)
    
    return total
    

def main():
    A = []
    with open('2024/data/a11.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file][0]
    A = [int(a) for a in A.split(' ')]

    print(get_score(A, 25))
    print(get_score(A, 75))


if __name__ == '__main__':
    main()
