
fH=open("puzzle.txt")
#fH=open("sample1.txt")
lines=fH.readlines()
fH.close()

MAZE={}
idx_row=-1
idx_col=-1
for line in lines:
    if line[-1:]=='\n':
        line=line[:-1]
    idx_row+=1
    idx_col=-1
    for c in line:
        idx_col+=1
        MAZE[(idx_row,idx_col)]=c

row_MAX=idx_row
col_MAX=idx_col
#col_MAX=len(MAZE)-1

print("row_MAX:", row_MAX)
print("col_MAX:", col_MAX)


def print_maze():
    for y in range(row_MAX+1):
        str_r=""
        for x in range(col_MAX+1):
            str_r+=MAZE[(y,x)]
        print(str_r)


max_ROLL_in8pos=3
CHAR_ROLL='@'

def get_roll_count_in_adjacent_8_pos(c_col, c_row):
    #print("\t:Given row:",c_row," col:",c_col)
    n_rollcount=0
    str_e=""
    #-------8 neighbors----
    range_POS=[]
    range_POS.append((c_row-1,c_col-1))
    range_POS.append((c_row-1,c_col))
    range_POS.append((c_row-1,c_col+1))
    range_POS.append((c_row,c_col-1))
    #range_POS.append((c_row,c_col))
    range_POS.append((c_row,c_col+1))
    range_POS.append((c_row+1,c_col-1))
    range_POS.append((c_row+1,c_col))
    range_POS.append((c_row+1,c_col+1))
    #--------------------------
    for i_row,i_col in range_POS:
        if i_col>=0 and i_col<= col_MAX and i_row>=0 and i_row<=row_MAX:
            str_e+="\t:searching row-"+str(i_row)+" col-"+str(i_col)
            if MAZE[(i_row,i_col)]==CHAR_ROLL:
                str_e+=": found"
                n_rollcount += 1
            str_e+="\n"

    #print(str_e)
    return n_rollcount

def do_roll_substitution(lst_row_col):
    for r,c in lst_row_col:
        MAZE[(r,c)]='x'

def do_maze_solve_for_roll8neighbour():
    count_r=0
    f_lrowcol=[]
    for row in range(0, row_MAX+1):
        r_count=[]
        for col in range(0, col_MAX+1):
            if MAZE[(row, col)]==CHAR_ROLL:
                n_count = get_roll_count_in_adjacent_8_pos(col, row)
                if n_count < 4:
                    r_count.append((row,col))
                    f_lrowcol.append((row,col))
        count_r+=len(r_count)
        #print("\t:Total for row-",row,":",len(r_count))
    print("\t: total ROLLS:",count_r)
    return count_r,f_lrowcol


res=1
f_pos=[]
f_num=0
tries=0
while(res):
    f_num,f_pos=do_maze_solve_for_roll8neighbour()
    res == f_num>0
    if f_num==0:
        res=0
        #exit()
    else:
        tries += f_num
        do_roll_substitution(f_pos)
        f_pos=[]

print("FINAL ROLLS:",tries)
