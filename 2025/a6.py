from collections import defaultdict
import numpy as np

def p1(A):
    num_dict = defaultdict(list)
    symbols = {}
    for row in A:
        nums = row.split(' ')
        cnt = 0
        for num in nums:
            if num.isnumeric():
                num_dict[cnt].append(int(num))
                cnt += 1
            elif num in ('+', '*'):
                symbols[cnt] = num
                cnt += 1
            else:
                continue

    result = 0
    for i, nlist in num_dict.items():
        if symbols[i] == '*':
            result += np.prod(nlist)
        else:
            result += sum(nlist)
    print(result)


def p2(A):
    result = 0
    buffer = []
    operator = None
    for i in range(len(A[0])):
        num_str = ''

        for row in A:
            if i >= len(row):
                break
            if row[i] == '+':
                operator = '+'
            elif row[i] == '*':
                operator = '*'
            elif row[i].isnumeric():
                num_str += row[i]

        if num_str == '':
            if operator == '*':
                result += np.prod(buffer)
            else:
                result += sum(buffer)
            buffer = []           
        else:
            buffer.append(int(num_str))
    print(result)


def main():
    A = []
    with open('data/a6.txt', 'r', encoding='UTF-8') as file:
        A = [line for line in file]
    p1(A)
    p2(A)


if __name__ == '__main__':
    main()