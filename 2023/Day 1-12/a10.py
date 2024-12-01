V = [{'7':(-1,0,1), '|':(0,-1,0), 'F': (1,0,2)}, {'F':(0,1,3), '-':(-1,0,1), 'L': (0,-1,0)},
     {'7':(0,1,3), '-':(1,0,2), 'J': (0,-1,0)}, {'J':(-1,0,1), '|':(0,-1,3), 'L': (1,0,2)}]

S = [('7','|','F'), ('7','F','L'), ('J','7','-'), ('|','L','J')]
S1 = [(0,-1), (-1,0), (1,0), (0,1)]

sym = {'F':'....F-.|.', '7':'...-7..|.', 'L':'.|..L-...','J':'.|.-J....','|':'.|..|..|.', '-':'...---...', '.':'.........', 'S':'...-S-...'}
s_help = [(1,'|'), (3,'-'), (5,'-'), (7,'|')]

def part_2(A, start_pos, main_loop):
    ### Expand map
    new_map = []
    added_dots = 0
    total_dots = 0
    for y in range(len(A)):
        B = ['', '', '']
        for x in range(len(A[0])):
            key = A[y][x] if (x,y) in main_loop else '.'
            for i in range(3):
                B[i] += sym[key][i*3:i*3+3]
            added_dots += sym[key].count('.')-key.count('.')
            total_dots += sym[key].count('.')
        new_map.extend(B)

    ### Try to visit all dots
    visited = set()
    visited_A = set()
    visit_list = {start_pos}
    while len(visit_list) > 0:
        node = visit_list.pop()
        visited.add(node)
        for i in range(4):
            pos = ((node[0]+S1[i][0],node[1]+S1[i][1]))
            if pos in visited or pos[0] < 0 or pos[0] >= len(new_map[0]):
                continue
            if pos[1] < 0 or pos[1] >= len(new_map):
                continue
            if new_map[pos[1]][pos[0]] == '.':
                visit_list.add(pos)
                visited_A.add((pos[0]//3, pos[1]//3))
    
    ### Count not visited
    counter = 0
    for y, row in enumerate(A):
        for x, cell in enumerate(row):
            if (x,y) not in visited_A:
                counter += 1
    print(counter)

def main():
    A = []
    main_loop = set()
    with open('2023/data/a10.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]

    ### Find startpoint
    pos = (0,0)
    dir = 0
    start_pos = (0,0)
    for y, line in enumerate(A):
        for x, char in enumerate(line):
            if char == 'S':
                start_pos = (x,y)
                s_symbol = ['.','.','.','.','S','.','.','.','.']
                for i in range(4):
                    if A[y+S1[i][1]][x+S1[i][0]] in S[i]: 
                        dir = i
                        s_symbol[s_help[i][0]] = s_help[i][1]
                sym['S'] = "".join(s_symbol)
                break
    
    pipe_len = 0
    pos = start_pos
    
    while True:
        pipe_len += 1
        main_loop.add(pos)
        pos = (pos[0]+S1[dir][0], pos[1]+S1[dir][1])
        if pos == start_pos:
            break
        vec = V[dir].get(A[pos[1]][pos[0]])
        dir = vec[2]

    print(pipe_len//2)

    ### Part 2
    part_2(A, start_pos, main_loop)

if __name__ == '__main__':
    main()