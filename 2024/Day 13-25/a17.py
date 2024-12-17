A, B, C = 4,5,6


def exe(program, register):
    values = [0,1,2,3,*register]
    ip = 0
    out = []

    while ip < len(program):
        instr, co = program[ip], program[ip+1]
        if instr == 0:
            values[A] = values[A]//(2**values[co])
        elif instr == 1:
            values[B] = values[B]^co
        elif instr == 2:
            values[B] = values[co]%8
        elif instr == 3:
            if values[A] != 0:
                ip = co
                continue
        elif instr == 4:
            values[B] = values[B]^values[C]
        elif instr == 5:
            out.append(str(values[co]%8))
        elif instr == 6:
            values[B] = values[A]//(2**values[co])
        elif instr == 7:
            values[C] = values[A]//(2**values[co])
        ip += 2
    return "".join(out)


def main():
    vector = []
    with open('2024/data/a17.txt', 'r', encoding='UTF-8') as file:
        vector = [line.strip() for line in file]
    
    program = [int(x) for x in vector[4][9:].split(',')]
    register = [int(x[11:]) for x in vector[:3]]
    target = "".join([str(x) for x in program])
    G = [0]

    ### Part 1
    print(",".join(list(exe(program, register))))
    
    ### Part 2
    counter = 0
    for i in range(len(target)-1, -1, -1):
        counter +=1
        t = target[i:]
        new_G = []
        for g in G:
            g *= 8
            for i in range(0,8):
                rA = g+i
                register[0] = rA
                res = exe(program, register)
                if res == t:
                    new_G.append(rA)
        G = new_G
    G.sort()
    print(sorted(G)[0])


if __name__ == '__main__':
    main()
