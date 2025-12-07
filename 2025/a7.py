def p12(A:list[str]):
    si = A[0].find('S')
    beams = [0 for _ in range(len(A[0]))]
    beams[si] += 1
    cnt = 0

    for i in range(1, len(A)):
        for j, sym in enumerate(A[i]):
            if beams[j] == 0:
                continue
            if sym == '^':
                beams[j+1] += beams[j]
                beams[j-1] += beams[j]
                beams[j] = 0
                cnt += 1

    print(cnt)
    print(sum(beams))

def main():
    A = []
    with open('data/a7.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]

    p12(A)
    

if __name__ == '__main__':
    main()
