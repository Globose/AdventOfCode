
def get_max_idx(nums, rspace):
    max1 = max(nums[:len(nums)-rspace])
    index = nums.index(max1)
    return index

def p1(A):
    nsum = 0
    for seq in A:
        nums = [int(i) for i in seq]
        max1 = max(nums[:len(nums)-1])
        index = nums.index(max1)
        max2 = max(nums[index+1:])
        nsum += max1*10+max2
    print(nsum)

def p2(A):
    nsum = 0
    for seq in A:
        nums = [int(i) for i in seq]
        nnum = 0
        for i in range(12):
            idx = get_max_idx(nums, 12-i-1)
            nnum += nums[idx]*(10**(12-i-1))
            nums = nums[idx+1:]
        nsum += nnum
    print(nsum)

def main():
    A = []
    with open('data/a3.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]

    # p1(A)
    p2(A)
    

if __name__ == '__main__':
    main()