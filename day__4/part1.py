
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



max_ROLL_in8pos=3
CHAR_ROLL='@'

def get_roll_count_in_adjacent_8_pos(c_col, c_row):
    print("\t:Given row:",c_row," col:",c_col)
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


count_r=0
for row in range(0, row_MAX+1):
    r_count=[]
    for col in range(0, col_MAX+1):
        if MAZE[(row, col)]==CHAR_ROLL:
            n_count = get_roll_count_in_adjacent_8_pos(col, row)
            if n_count < 4:
                r_count.append((col,row))
    count_r+=len(r_count)
    #while(col<=col_MAX-4):
    #        n_count,r_count = get_roll_count_in_adjacent_8_pos(col, row)
    #    if n_count < 4:
    #        count_r+=r_count
    #    col+=4
    print("Total for row-",row,":",len(r_count))
    for x,y in r_count:
        print("\t:(",x,",",y,")")

print("TOTAL ROLLS:",count_r)
