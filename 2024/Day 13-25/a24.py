def calc(p1, p2, op):
    if op == 'AND':
        return p1&p2
    if op == 'XOR':
        return p1^p2
    return p1|p2

def get_bin(c, values):
    Z = []
    for key in values:
        if key[0] == c:
            Z.append(key)
    Z.sort(reverse=True)

    s = ""
    for z in Z:
        s += str(values[z])
    return s

def part1(A, div, values):
    B = []    
    for a in A[div+1:]:
        a2 = a.split(' ')
        a4 = a2[4]
        B.append((a2[0], a2[2], a2[1], a4, a))

    while len(B) > 0:
        C = []
        for b in B:
            if b[0] in values and b[1] in values:
                values[b[3]] = calc(values[b[0]], values[b[1]], b[2])
            else:
                C.append(b)
        B = C
    print(int(get_bin('z', values), 2))

def num(n):
    if n < 10:
        return '0'+str(n)
    return str(n)

def part2(A, div, values):
    C = {}
    for a in A[div+1:]:
        u = a.split(' ')
        C[u[0]+u[1]] = a
        C[u[2]+u[1]] = a
        C[u[4]] = a

    ### Find alpha and r
    alpha = []
    rv = []
    for x in values.keys():
        if x[0] != 'x':
            continue
        x_alpha = C[x+'XOR']
        x_r = C[x+'AND']
        ax = x_alpha[-3:]
        rx = x_r[-3:]
        alpha.append(ax)
        rv.append(rx)
    
    swops = set()

    ### Find k
    k = []
    for i, a in enumerate(alpha):
        if i < 1:
            k.append(None)
            continue
        c = C.get(a+'XOR')
        if c is None:
            swops.add(a)
            c1 = C.get('z'+str(i))
            if c1:
                spl = c1.split(' ')
                if spl[0] in rv:
                    swops.add(spl[0])
                elif spl[2] in rv:
                    swops.add(spl[2])
            k.append(None)
            continue
        if c[-3] != 'z':
            swops.add(c[-3:])
            swops.add('z'+num(i))
            k.append(None)
        else:
            if a != c[8:11]:
                k.append(c[8:11])
            else:
                k.append(c[:3])

    print(",".join(sorted(swops)))

def main():
    A = []
    with open('2024/data/a24.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    div = A.index('')
    values = {}

    for a in A[:div]:
        a2 = a.split(': ')
        values[a2[0]] = int(a2[1])
    
    part1(A, div, values)
    part2(A, div, values)
            

if __name__ == '__main__':
    main()
