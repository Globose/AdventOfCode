import numpy as np
import re

def solve(v1, v2, sol):
    a1 = np.array([[v1[0], v2[0]],[v1[1], v2[1]]])
    a2 = np.array([sol[0], sol[1]])
    rank = np.linalg.matrix_rank(a1)
    if rank == 2:
        k1, k2 = np.linalg.solve(a1,a2)
        if k1 >= 0 and k2 >= 0:
            k1, k2 = int(k1+.1), int(k2+.1)
            x = int(v1[0]*k1+v2[0]*k2)
            y = int(v1[1]*k1+v2[1]*k2)
            if x == sol[0] and y == sol[1]:
                return (k1,k2)
    return None


def main():
    A = []
    with open('2024/data/a13.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    
    i = 0
    tokens = [0,0]
    while i < len(A):
        v1 = tuple([int(x) for x in re.findall(r"\d+", A[i])])
        v2 = tuple([int(x) for x in re.findall(r"\d+", A[i+1])])
        prize = tuple([int(x) for x in re.findall(r"\d+", A[i+2])])
        
        ### part 1
        solved = solve(v1, v2, prize)
        if solved:
            tokens[0] += solved[0]*3+solved[1]

        ### part 2
        plus = 10000000000000
        prize = (prize[0]+plus, prize[1]+plus)
        solved = solve(v1, v2, prize)
        if solved:
            tokens[1] += solved[0]*3+solved[1]
        i+=4
    print(f"{tokens[0]} \n{tokens[1]}")


if __name__ == '__main__':
    main()
