f=open("../puzzle.txt")
fLines=f.readlines()
f.close()

n_pos=[(int(c[0]),int(c[1])) for c in [line.split('\n')[0].split(',') for line in fLines]]

x_coord=[p[0] for p in n_pos]
x_coord.sort()
x_makeUnq={v:-1 for v in x_coord}
x_compress={v:idx for idx,v in enumerate(x_makeUnq)}
rev_X={idx:v for v,idx in x_compress.items()}
x_MAX=[mIdx for idx,mIdx in enumerate(rev_X.keys()) if idx==len(rev_X.keys())-1][0]

y_coord=[p[1] for p in n_pos]
y_coord.sort()
y_makeUnq={v:-1 for v in y_coord}
y_compress={v:idx for idx,v in enumerate(y_makeUnq)}
rev_Y = {idx:v for v,idx in y_compress.items()}
y_MAX=[mIdx for idx,mIdx in enumerate(rev_Y.keys()) if idx==len(rev_Y.keys())-1][0]


print("x_MAX:",x_MAX)
print("y_MAX:",y_MAX)

m_grid=[]
for y in range(0,y_MAX+1):
    m_grid.append([0*x for x in range(0,x_MAX+1)])

def draw_lines(pos1, pos2):
    begX = min(x_compress[pos1[0]], x_compress[pos2[0]])
    endX = max(x_compress[pos1[0]], x_compress[pos2[0]])
    begY = min(y_compress[pos1[1]], y_compress[pos2[1]])
    endY = max(y_compress[pos1[1]], y_compress[pos2[1]])
    if begX == endX:
        for i in range(begY,endY+1):
            m_grid[i][begX] = 2
        m_grid[endY][begX]=1
    elif begY==endY:
        for i in range(begX,endX+1):
            if m_grid[begY][i] == 0:
                m_grid[begY][i] = 1
    else:
        print("BAD CASE FOR DRAW LINE in", pos1,pos2)
        exit()

# create a boundary lines
for pIdx in range(0, len(n_pos)):
    if pIdx == len(n_pos)-1: #last entry
        draw_lines(n_pos[pIdx], n_pos[0])
    else:
        draw_lines(n_pos[pIdx], n_pos[pIdx+1])

# fill the polygonal interior area
for r_idx in range(0, y_MAX+1):
    parity=0
    for c_idx in range(0, x_MAX+1):
        if m_grid[r_idx][c_idx] == 2:
            parity ^= 1
        elif parity == 1:
            m_grid[r_idx][c_idx] = 1

##==========================================
## PRINT GRID ##
##==========================================
#l_grid='\n PRINT GRID \n'
#for r_idx in range(0, y_MAX+1):
#    for c_idx in range(0, x_MAX+1):
#        l_grid += str(m_grid[r_idx][c_idx])
#    l_grid += '\n'
#print(l_grid)
##==========================================


# prefix sum for cols
m_col_sums=[]
# fill the list with 2-D zeros
for y in range(0,y_MAX+1):
    m_col_sums.append([0 for _ in range(0,x_MAX+1)])
# iterate over each column-index (for each col, add list of sum for preceeding-ROWs)
for col_IDX in range(0, x_MAX+1):
    sqArea_BEG = -1
    for row_IDX in range(0,y_MAX+1):
        if m_grid[row_IDX][col_IDX] == 0:
            sqArea_BEG = -1
        else:
            if sqArea_BEG == -1:
                sqArea_BEG = rev_Y[row_IDX]
                #print("\t: using row:",row_IDX,"rev_Y[row]:",rev_Y[row_IDX])
            m_col_sums[row_IDX][col_IDX] = rev_Y[row_IDX] - sqArea_BEG + 1

##==========================================
##  PRINT COL SUM
##==========================================
#for col_IDX in range(0, x_MAX+1):
#    for row_IDX in range(0,y_MAX+1):
#        print("Sum of row:",row_IDX,"col:",col_IDX,"=",m_col_sums[row_IDX][col_IDX])
##==========================================

#print("Printing N_POS")
#for pos in n_pos:
#    print(pos)


m_answer = 1
# solve for largest area
for idx1,pos1 in enumerate(n_pos):
    for idx2 in range(idx1+1, len(n_pos)):
        pos2 = n_pos[idx2]
        # flag to check if the point-PAIR can be used
        is_good = 1
        # calculare the next post to consider for the point-PAIR
        if pos1[1] < pos2[1]: # swap if POS1-y-pos is smaller than y-pos of POS2
            tmp = pos1
            pos1 = pos2
            pos2 = tmp
        # The AREA-rectangle HEIGHT
        need_height = abs(pos2[1] - pos1[1]) + 1
        # get the START and END x-pos for rect-area calc
        xCompBeg = x_compress[pos1[0]]
        xCompEnd = x_compress[pos2[0]]
        # Y-axis value for the Rectangle considered
        y_RECT = y_compress[pos1[1]]
    
        #print("For start:",pos1,"and end:", pos2)
        #print("\t: xCompBeg:", xCompBeg)
        #print("\t: xCompEnd:", xCompEnd)
        #print("\t: y_RECT:", y_RECT)
    
        if xCompBeg < xCompEnd:
            for idxC in range(xCompBeg, xCompEnd+1):
                if m_grid[y_RECT][idxC] == 0 or m_col_sums[y_RECT][idxC] < need_height:
                    is_good = 0
                    break
        else:
            for cIDX in range(xCompBeg, xCompEnd-1, -1):
                if m_grid[y_RECT][cIDX] == 0 or m_col_sums[y_RECT][cIDX] < need_height:
                    is_good = 0
                    break
        if is_good:
            s0 = abs(pos2[0] - pos1[0]) + 1
            s1 = abs(pos2[1] - pos1[1]) + 1
            m_answer = max(m_answer, s0*s1)

print("Result:", m_answer)
