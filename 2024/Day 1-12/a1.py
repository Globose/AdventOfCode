from collections import Counter

def main():
    A = []
    with open('2024/data/a1.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    C1 = []
    C2 = []
    for row in A:
        lst = row.split('   ')
        C1.append(int(lst[0]))
        C2.append(int(lst[1]))
    C1_s = sorted(C1)
    C2_s = sorted(C2)

    diff = 0
    for i in range(len(C1_s)):
        diff += abs(C1_s[i]-C2_s[i])
    print(diff)

    ### Part 2
    c = Counter(C2)
    score = 0
    for n in C1:
        score += n*c.get(n, 0)
    print(score)

    

if __name__ == '__main__':
    main()