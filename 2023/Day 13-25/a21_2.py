from collections import deque

DIR = ((1,0), (0,1), (-1,0), (0,-1))

class Node:
    def __init__(self, x, y, value) -> None:
        self.value = value
        self.x = x
        self.y = y
        self.neighbors = []

    def add_neighbors(self, nodes):
        for d in DIR:
            neigbor = nodes.get((self.x+d[0],self.y+d[1]))
            if neigbor:
                self.neighbors.append(neigbor)

    def get_cords(self):
        return (self.x,self.y)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple):
            return (self.x, self.y) == other
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}) = {self.value}"

    def __str__(self) -> str:
        return f"{self.value}"

class Grid:
    def __init__(self, grid) -> None:
        self.grid = {}
        self.width = len(grid[0])
        self.height = len(grid)
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                n = Node(x,y,cell)
                self.grid[n] = n

        for node in self.grid:
            node.add_neighbors(self.grid)
    
    def __repr__(self) -> str:
        s = ""
        for y in range(self.height):
            row = []
            for x in range(self.width):
                s += str(self.grid.get((x,y)))
            s += "\n"
        return s
    
    def get_value(self, value):
        """Returns a square in the grid with a value"""
        for node in self.grid:
            if node.value == value:
                return node
    
    def set_value(self, x, y, value):
        for node in self.grid:
            if node.x == x and node.y == y:
                node.value = value
                return
    
    def count(self, value):
        """Returns the number of nodes in the grid with a given value"""
        counter = 0
        for node in self.grid:
            if node.value == value:
                counter += 1
        return counter

def arithmetic_sum(h, l=1):
    """Returns arithmetic sum between low and high"""
    return int(0.5*(h-l+1)*(h+l))

def poly(x, y, plen, odd, draw=False):
    mult = 1
    rx = 0
    ry = 0
    A = []
    with open('2023/data/a21.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    for i in range(len(A)):
        A[i] = A[i]*mult
    B = []
    for i in range(mult):
        B.extend(A)

    grid = Grid(B)
    d = deque()
    grid.set_value(65,65,".")
    grid.set_value(x+rx*(mult//2), y+rx*(mult//2),"S")
    d.append((grid.get_value("S"), 0))

    plot_counter = 0
    while len(d) > 0:
        plot, path_len = d.popleft()
        if path_len > 131*(mult//2)+plen:
            break
        if plot.value != '.' and plot.value != 'S' and plot.value != 'P':
            continue
        if path_len%2 == odd:
            plot_counter += 1
        plot.value = 0

        d.extend([(x,path_len+1) for x in plot.neighbors])

    if draw:
        print(grid)
    return plot_counter

def main():
    q = 4*25*7*17*17*131
    n = q//131

    b = arithmetic_sum(n-1)*2+n
    o = arithmetic_sum(n-2)*2+n-1

    o_size = poly(65,65,200,1)
    b_size = poly(65,65,200,0)

    b *= b_size
    o *= o_size
    
    ox_corners = []
    bx_diag = []
    ox_diag = []

    b_vars = ((0,0,65), (130,0,65), (130,130,65), (0,130,65))
    o_vars = ((0,0,195), (130,0,195), (130,130,195), (0,130,195))
    o_corn = ((65,0,130), (0,65,130), (65,130,130), (130,65,130))
    for i in range(4):
        bx_diag.append(poly(b_vars[i][0],b_vars[i][1],b_vars[i][2],0, False))
        ox_diag.append(poly(o_vars[i][0],o_vars[i][1],o_vars[i][2],1, False))
        ox_corners.append(poly(o_corn[i][0],o_corn[i][1],o_corn[i][2],0, False))
    
    # print(bx_diag)
    # print(ox_diag)
    # print(ox_corners)

    total = b + o + sum(bx_diag)*n + sum(ox_diag)*(n-1)+sum(ox_corners)
    print(total)

if __name__ == '__main__':
    main()
