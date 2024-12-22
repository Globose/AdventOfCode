from collections import defaultdict

def mix(s_num, t):
    return (t^s_num) % 16777216

def next(s_num, k, d, index):
    seq = []
    last = int(str(s_num)[-1])
    for _ in range(k):
        s_num = mix(s_num, s_num*64)
        s_num = mix(s_num, s_num//32)
        s_num = mix(s_num, s_num*2048)

        new = int(str(s_num)[-1])
        diff = new-last
        last = new
        seq.append(diff)
        if len(seq) > 4:
            seq.pop(0)
        if len(seq) == 4:
            dct = d[tuple(seq)]
            if index not in dct:
                dct[index] = last
    return s_num

def main():
    A = []
    with open('2024/data/a22.txt', 'r', encoding='UTF-8') as file:
        A = [int(line.strip()) for line in file]
    
    d = defaultdict(dict)
    total = 0
    for i, x in enumerate(A):
        total += next(x,2000,d, i)
    print(total)

    max_value = 0
    for items in d.items():
        s = sum(items[1].values())
        if s > max_value:
            max_value = s
    
    print(max_value)
    
if __name__ == '__main__':
    main()
