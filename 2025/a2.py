
def p1(nums):
    result = []
    for pair in nums:
        num_low, num_end = int(pair[0]), int(pair[1])
        num_len = max(1, (len(pair[0]))//2)
        num0 = int(pair[0][:num_len])
        num1 = int(str(num0)*2)

        while num1 <= num_end:
            if num1 >= num_low:
                result.append(num1)
            num0 += 1
            num1 = int(str(num0)*2)

    print(sum(result))

def p2(nums):
    max_num = max([int(x[1]) for x in nums])
    
    i = 1
    repeating = set()
    while True:
        base_num = str(i)
        if int(base_num*2) > max_num:
            break

        num = base_num*2
        while int(num) < max_num:
            repeating.add(int(num))
            num += base_num

        i+=1

    result = set()
    for pair in nums:
        num_low, num_end = int(pair[0]), int(pair[1])
        for i in repeating:
            if num_low <= i <= num_end:
                result.add(i)
    print(sum(result))

    

def main():
    A = []
    with open('data/a2.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    A = [x.split('-') for x in A[0].split(',')]
    
    p1(A)
    p2(A)


if __name__ == '__main__':
    main()