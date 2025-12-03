
fH=open("sample1.txt",'r')
fLines=fH.readlines()
lines=[]
for l in fLines:
    lines.append(l.strip())

def do_move(i_pos, mov):
    o_pos=i_pos
    # rotations
    n_rot=0
    # given move dir and value
    m_dir=mov[0]
    m_val=int(int(mov[1:]))
    # extract the val removing roations; store rotations
    c_mov=m_val%(99+1)
    n_rot=int(m_val/(99+1))
    # add or subtract; use a -1
    coeff=0;
    if mov[0]=='R':
        coeff=1
    elif mov[0]=='L':
        coeff=-1
    else:
        print("BAD")
    o_pos=i_pos + coeff*c_mov
    has_crossed_zero=False
    if o_pos < 0:
        o_pos = 100 + o_pos
    elif o_pos > 99:
        o_pos = o_pos - 100
    # has landed at ZERO
    n_zero = n_rot
    if o_pos==0:
        n_zero+=1
    else: # crossed zero
        if o_pos < i_pos or has_crossed_zero:
            n_zero+=1
    print(i_pos, mov,"->", o_pos)
    return o_pos, n_zero

inp_pos=50
out_pos=inp_pos
tot_zero=0
for mov_l in lines:
    out_pos, num_0 = do_move(inp_pos, mov_l)
    tot_zero += num_0
    inp_pos = out_pos

print("Zeros:", tot_zero)
