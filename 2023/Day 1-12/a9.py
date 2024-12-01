def interp(A):
    diff_list = [A[i]-A[i-1] for i in range(1,len(A))]
    if not all(x == 0 for x in diff_list):
        interp(diff_list)
    A.append(diff_list[-1]+A[-1])

def interp_backwards(A):
    diff_list = [A[i]-A[i-1] for i in range(1,len(A))]
    if not all(x == 0 for x in diff_list):
        interp_backwards(diff_list)
    A.insert(0,A[0]-diff_list[0])

def main():
    A = []
    with open('2023/data/a9.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    series = []
    for s in A:
        series.append([int(x) for x in s.split(" ")])

    total = 0
    for serie in series:
        interp(serie)
        total += serie[-1]
        serie.pop()
    print(total)

    ### Part 2
    total = 0
    for serie in series:
        interp_backwards(serie)
        total += serie[0]
    print(total)

if __name__ == '__main__':
    main()