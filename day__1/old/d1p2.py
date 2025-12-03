
file_lines=[]
with open("sample2.txt",'r') as fH:
    file_lines = [list(line.strip()) for line in fH]


def get_pos_from_move_line(move_line, pos_in, n_zeros):
    pos_out=-99
    str_val=""
    for c in move_line:
        str_val+=c
    val=int(str_val[1:])
    #print("Processing", str_val, "with", pos_in,"...")
    dir=str_val[0]
    # Make sure that it handles val that is G.T. 99:
    n_rotations = int(val / (99 + 1))
    val = val % (99 + 1) 
    if dir=='L':
        pos_out = pos_in - val
        if pos_out < 0:
            pos_out = 99 + pos_out + 1
    elif dir=='R':
        pos_out=pos_in+val
        if pos_out>99:
            pos_out = pos_out%99 - 1
    else:
        print("BAD BAD DATA: " , dir)
    if 0==pos_out:
        n_zeros+=1
    # part 2 wants to consider the times the dial crosses zero
    # this happens when :
    # multiple-of-99+1 rotations are made
    # R-VAL such thant pos_out +  R-VAL > 99+1
    # L-VAL such that pos_in < L-VAL
    if pos_in==0 and n_rotations>1 and val>0:
        n_rotations +=1
    #------------------------------------------------------------------------
    if pos_out!=0 and pos_in!=0:
        if dir=='R' and pos_in + val > 99+1:
            n_rotations += 1
        elif dir=='L' and pos_in < val:
            n_rotations += 1
    #------------------------------------------------------------------------
    n_zeros += n_rotations
    #------------------------------------------------------------------------
    print_str = str_val + " with " + str(pos_in) + " -> " + str(pos_out) 
    #------------------------------------------------------------------------
    rotn_str=" no "
    if n_rotations > 0:
        rotn_str = str(n_rotations)
    #------------------------------------------------------------------------
    print_str += " and " + str(n_rotations) + " extra rotations"
    print(print_str)
    return pos_out, n_zeros



n_zeros=0
pos_x=50
old_pos=pos_x
o_line=""
for mline in file_lines:
    pos_x, n_zeros = get_pos_from_move_line(mline, pos_x, n_zeros)
    old_pos=pos_x
    o_line=mline

print("N ZEROS:", n_zeros)
