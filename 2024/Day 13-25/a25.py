def get_col(key, n):
    ht = -1
    for row in key:
        if row[n] == '#':
            ht += 1
    return ht

def main():
    A = []
    with open('2024/data/a25.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    
    key = []
    locks = []
    keys = []
    for row in A:
        if row == '':
            if key[0] == '#####':
                locks.append(key)
            else:
                keys.append(key)
            key = []
        else:
            key.append(row)
    keys.append(key)
    
    fit = 0
    for lock in locks:
        for key in keys:
            ol = True
            for i in range(5):
                keyc = get_col(key, i)
                lockc = get_col(lock, i)
                if keyc + lockc > 5:
                    ol = False
            if ol:
                fit += 1
    print(fit)
    

if __name__ == '__main__':
    main()