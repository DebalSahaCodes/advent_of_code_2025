
file_lines=[]
with open("puzzle.txt",'r') as fH:
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
    val = val % (99 + 1) # +1 for the fact that it starts at 0 so actually 100 clicks in one rotation
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
    print(str_val, "with", pos_in, "->", pos_out)
    return pos_out, n_zeros



n_zeros=0
pos_x=50
for mline in file_lines:
    pos_x, n_zeros = get_pos_from_move_line(mline, pos_x, n_zeros)

print("N ZEROS:", n_zeros)
