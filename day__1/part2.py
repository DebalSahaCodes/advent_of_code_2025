
fH=open("puzzle.txt",'r')
fLines=fH.readlines()
lines=[]
for l in fLines:
    lines.append(l.strip())


def do_count(count, coeff, init):
    n_zero=0
    next=init
    for _ in range(count):
        next=init + coeff
        if next>99:
            next=0
        elif next<0:
            next=99
        if next == 0:
            n_zero+=1
        init=next
    return next,n_zero


def do_move(i_pos, mov):
    n_zero=0
    # rotations
    n_rot=0
    # given move dir and value
    m_dir=mov[0]
    m_val=int(int(mov[1:]))
    coeff=0;
    if mov[0]=='R':
        coeff=1
    elif mov[0]=='L':
        coeff=-1
    else:
        print("BAD")
    o_pos, n_zero = do_count(m_val, coeff, i_pos)
    print(i_pos, mov,"->", o_pos,"zeros:",n_zero)
    return o_pos, n_zero, 0

inp_pos=50
out_pos=inp_pos
tot_zero=0
for mov_l in lines:
    out_pos, num_0, num_r = do_move(inp_pos, mov_l)
    tot_zero += num_0 + num_r
    inp_pos = out_pos

print("Zeros:", tot_zero)
