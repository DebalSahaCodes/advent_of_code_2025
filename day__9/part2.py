
#fH=open("puzzle.txt",'r')
fH=open("sample.txt",'r')
f_lines=fH.readlines()
fH.close()

n_lines=[]# remove '\n'
for line in f_lines:
    if line[-1:]=='\n':
        line=line[:-1]
    n_lines.append(line)

x_MAX=-1
y_MAX=-1
# generate_posList_from_lines(line)
n_pos=[]
for idx,line in enumerate(n_lines):
    n_pos.append([int(c) for c in line.split(',')])
    if n_pos[idx][0] > x_MAX:
        x_MAX = n_pos[idx][0]
    if n_pos[idx][1] > y_MAX:
        y_MAX = n_pos[idx][1]

print('x_MAX:',x_MAX)
print('y_MAX:',y_MAX)
#exit()

def is_present_in_NPOS(pos):
    is_found=0
    for p_pos in n_pos:
        if pos[0]==p_pos[0] and pos[1]==p_pos[1]:
            is_found=1
            break
    return is_found


m_maze={}
is_found=0
def generate_maze_red_green():
    for y in range(0, y_MAX+1):
        is_on_off=0
        is_found=0
        for x in range(0, x_MAX+1):
            c_pos=(x,y)
            if is_present_in_NPOS(c_pos):
                #print("\t:FOUND:",c_pos)
                #exit()
                if not is_on_off:
                    is_on_off=1
                    #print("\t:setting...")
                    is_found=1
                else:
                    #print("\t:re-setting...")
                    is_on_off=0
            if is_on_off or is_found:
                m_maze[c_pos]='X'
            else:
                m_maze[c_pos]='.'
            #print("\nAdding (",x,',',y,'):',m_maze[c_pos])
generate_maze_red_green()

def is_valid_for_area(p1,p2):
    if p1[0] == p2[0] or p1[1]==p2[1]:
        #print("\t:Invalid if X same OR Y same")
        return 0
    # if P1-P2 is one diagonal then check opposite diagonal
    # (P1x,P1y) - (P2x,P2y) : main diagonal
    # (P1x,P2y) - (P2x,P1y) : opposite diagonal
    p_opp1=[p1[0],p2[1]]
    p_opp2=[p2[0],p1[1]]
    is_red_green_1=m_maze[(p_opp1[0], p_opp1[1])]=='X'
    is_red_green_2=m_maze[(p_opp2[0], p_opp2[1])]=='X'
    #print("\t:is_red_green", p_opp1,":",is_red_green_1)
    #print("\t:is_red_green", p_opp2,":",is_red_green_2)
    return is_red_green_1 and is_red_green_2


def get_dist_bw_pos1_pos2(pos1,pos2):
    dist2=0
    for i in range(0,2):
        val = pos2[i] - pos1[i]
        dist2+= val*val
    return dist2

dict_dist={}

def get_area_from_pair(g_pair):
    x=g_pair[0][0] - g_pair[1][0]
    if x<0:
        x = x*-1
    x = x+1
    y=g_pair[0][1] - g_pair[1][1]
    if y<0:
        y = y*-1
    y=y+1
    return x*y



b_area=0
b_pair=[]
b_line=[]
for idx1 in range(0, len(n_lines)):
    for idx2 in range(idx1, len(n_lines)):
        line1 = n_lines[idx1]
        line2 = n_lines[idx2]
        if idx1 != idx2:
            #print("processing",line1,"and",line2)
            p1=n_pos[idx1]
            p2=n_pos[idx2]
            if not is_valid_for_area(p1,p2):
                #print("\t:Invalid PAIR!")
                continue
            a12 = get_area_from_pair([p1,p2])
            #print("\t:Area:", a12)
            if a12 > b_area:
                b_area=a12
                b_pair=[]
                b_pair.append(p1)
                b_pair.append(p2)
                b_line=[]
                b_line.append(line1)
                b_line.append(line2)


if not b_pair:
    exit()
print("Biggest Area from ",b_line,':',get_area_from_pair(b_pair))
