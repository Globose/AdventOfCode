def get_data(n):
    A = []
    with open('2023/data/a6.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        for s in file:
            A.append(s.strip("\n"))
    
    nums = []
    n_str = []
    for row in A:
        e = row.split(' ')
        for str in e[1:]:
            if len(str) > 0:
                nums.append(int(str.strip()))
                n_str.append(str.strip())
    if n == 1:
        return [(nums[0],nums[4]), (nums[1],nums[5]), (nums[2],nums[6]), (nums[3],nums[7])]
    num1 = n_str[0]+n_str[1]+n_str[2]+n_str[3]
    num2 = n_str[4]+n_str[5]+n_str[6]+n_str[7]
    return (int(num1), int(num2))


def p1():
    data = get_data(1)
    
    margin = 1
    for x in data:
        times = []
        for i in range(x[0]+1):
            d = (x[0] - i)*i
            # print(i, d)
            if d > x[1]:
                times.append(i)

        m = max(times)-min(times)+1
        margin *= m

    print(margin)

def p2():
    data = get_data(2)

    n_1 = (int)(0.5*data[0]-(0.25*(data[0]**2)-data[1])**0.5+1)
    n_2 = (0.5*data[0]+(0.25*(data[0]**2)-data[1])**0.5)
    n_2_int = (int)(n_2)
    if n_2 - n_2_int == 0:
        n_2_int -=1
    n_1_int = (int)(n_1)

    gap = n_2_int-n_1_int+1
    print(gap)

p1()
p2()