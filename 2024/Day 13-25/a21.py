from functools import lru_cache

npos = {'7':(0,0), '8':(1,0),'9':(2,0),'4':(0,1),'5':(1,1),'6':(2,1),'1':(0,2),'2':(1,2),'3':(2,2),'0':(1,3),'A':(2,3), 0:(0,3)}
kpos = {'^':(1,0), 'A':(2,0), '<':(0,1), 'v':(1,1), '>':(2,1), 0:((0,0))}

edge_cases = {(2,0,1,1):'<v', #A -> v
              (2,0,0,1):'v<<', #A -> <
              (2,1,1,0):'<^', #> -> ^ 
              (1,1,2,0):'^>', #v -> A
              (0,1,2,0):'>>^', #< -> A
              (1,0,2,1):'v>'} #^ -> >

@lru_cache
def get_ptr(x0, y0, x1, y1):
    t1 = (x0,y0,x1,y1)
    if t1 in edge_cases:
        return edge_cases[t1]
    s0 = s1 = ""
    if x0 < x1:
        s0 += '>'*(x1-x0)
    elif x1 < x0:
        s0 += '<'*(x0-x1)
    if y0 < y1:
        s1 += 'v'*(y1-y0)
    elif y1 < y0:
        s1 += '^'*(y0-y1)
    
    if (x1, y0) == (0,0):
        return s1+s0
    return s0+s1


def get_ptrs(x0, y0, x1, y1, void):
    A = [('',x0,y0)]
    F = []
    while len(A) > 0:
        B = []
        for a in A:
            seq, x, y = a
            if x == x1 and y == y1:
                F.append(seq+"A")
                continue
            if x < x1 and (x+1, y) != void:
                B.append((seq+'>', x+1, y))
            elif x > x1 and (x-1, y) != void:
                B.append((seq+'<', x-1, y))
            
            if y < y1 and (x, y+1) != void:
                B.append((seq+'v', x, y+1))
            if y > y1 and (x, y-1) != void:
                B.append((seq+'^', x, y-1))
        A = B
    return F


def spx(code):
    return [xu+'A' for xu in code.split('A')[:-1]]


@lru_cache
def get_sseq(code, depth, max_depth):
    if depth == max_depth:
        return len(code)
    p3 = ""
    pos = kpos.get('A')
    for c in code:
        p3 += get_ptr(*pos, *kpos[c])+'A'
        pos = kpos[c]
    ss = 0
    for x9 in spx(p3):
        ss += get_sseq(x9, depth+1, max_depth)
    return ss


def get_seq(spos, code):
    pos = spos.get('A')
    F = []
    p1 = ""
    for c in code:
        ptrs = get_ptrs(*pos, *spos[c], spos[0])
        pos = spos[c]

        if len(F) == 0:
            F = ptrs
            continue

        nF = []
        for p in ptrs:
            for f in F:
                nF.append(f+p)
        F = nF
    return F


def complexity(code, depth):
    A = get_seq(npos, code)
    B = []
    for a in A:
        ss = 0
        for xs in spx(a):
            ss += get_sseq(xs, 0, depth)
        B.append(ss)
    
    num = int(code[:3])
    return min(B)*num


def main():
    A = []
    with open('2024/data/a21.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]

    print(sum([complexity(x, 2) for x in A]))
    print(sum([complexity(x, 25) for x in A]))


if __name__ == '__main__':
    main()
