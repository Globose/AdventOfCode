import re

def main():
    A = []
    with open('2024/data/a3.txt', 'r', encoding='UTF-8') as file:
        A = "".join([line.strip() for line in file])
    
    B = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", A)
    s = sum([int(x[0])*int(x[1]) for x in B])
    print(s)

    ### Part 2
    enabled = True
    B =  re.finditer(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", A)
    s = 0
    for d in B:
        match = d.group(0)
        if match[0] != 'm':
            enabled = match == 'do()'
        elif enabled:
            nums = match[4:-1].split(',')
            s += int(nums[0])*int(nums[1])
    print(s)

if __name__ == '__main__':
    main()