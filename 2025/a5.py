def p1(ranges, id_list):
    fcnt = 0
    for id in id_list:
        for r in ranges:
            if id in r:
                fcnt += 1
                break

    print(fcnt)

def p2(ranges:list[range]):
    mod_ranges = []

    for r1 in ranges:
        r1_ranges = [r1]
        for r2 in mod_ranges:
            for i, r1_sub in enumerate(r1_ranges):
                if r1_sub.start in r2:
                    r1_ranges[i] = range(r2.stop,r1_sub.stop)
                if (r1_sub.stop-1) in r2:
                    r1_ranges[i] = range(r1_sub.start, r2.start)

            # r2 in r1
            for i, r1_sub in enumerate(r1_ranges):
                if r2.start in r1_sub and (r2.stop-1) in r1_sub:
                    r1_ranges[i] = range(r1_sub.start, r2.start)
                    r1_ranges.append(range(r2.stop, r1_sub.stop))
                    break

        mod_ranges.extend(r1_ranges)
    
    total = sum([max(0, x.stop-x.start) for x in mod_ranges])
    print(total)

def main():
    A = []
    with open('data/a5ex.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    
    ranges = []
    id_list = []
    space = False

    for a in A:
        if a == '':
            space = True
        elif space:
            id_list.append(int(a))
        else:
            n1, n2 = [int(x) for x in a.split('-')]
            ranges.append(range(n1, n2+1))
    
    p1(ranges, id_list)
    p2(ranges)
    

if __name__ == '__main__':
    main()