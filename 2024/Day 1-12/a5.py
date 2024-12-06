def main():
    A = []
    with open('2024/data/a5.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    
    priority = {}
    p_index = 0
    
    for i, row in enumerate(A):
        if row == '':
            p_index = i
            break

        o1, o2 = [int(x) for x in row.split('|')]
        priority.setdefault(o2, set()).add(o1)
        
    scores = [0,0]
    for row in A[p_index+1:]:
        serie = [int(x) for x in row.split(',')]
        valid = True
        for i, x in enumerate(serie):
            for j in range(i+1,len(serie)):
                if serie[j] in priority.get(serie[i],[]):
                    serie[i], serie[j] = serie[j], serie[i]
                    valid = False
                    continue
        scores[valid] += serie[len(serie)//2]

    print(f"{scores[1]}\n{scores[0]}")


if __name__ == '__main__':
    main()
