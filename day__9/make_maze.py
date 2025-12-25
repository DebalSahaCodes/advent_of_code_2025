f_lines=[]
with open("sample.txt") as f:
    f_lines=f.readlines()

n_pos=[line.split('\n')[0].split(',') for line in f_lines]
n_pos=[(int(c[0]),int(c[1])) for c in n_pos]

x_MIN=-1
x_MAX=-1
y_MIN=-1
y_MAX=-1

#m_bdry={}
#for idx1,pos1 in enumerate(n_pos):
#    if y_MIN == -1 or pos1[1] < y_MIN:
#        y_MIN=pos1[1]
#    if pos1[1] > y_MAX:
#        y_MAX=pos1[1]
#    if x_MIN == -1 or pos1[0] < x_MIN:
#        x_MIN=pos1[0]
#    if pos1[0]>x_MAX:
#        x_MAX=pos1[0]
#    for idx2 in range(idx1+1,len(n_pos)+1):
#        if idx2 <= len(n_pos)-1:
#            pos2=n_pos[idx2]
#            if pos2[1] < y_MIN:
#                y_MIN=pos2[1]
#            if pos2[0]==pos1[0]:
#                xc=pos1[0]
#                y_inc=1
#                if pos2[1]<pos1[1]:
#                    y_inc=-1
#                for yc in range(pos1[1],pos2[1]+y_inc,y_inc):
#                    #c_maze[(xc,yc)]='X'
#                    m_bdry[(xc,yc)]=1
#            elif pos2[1]==pos1[1]:
#                yc=pos1[1]
#                x_inc=1
#                if pos2[0]<pos1[0]:
#                    x_inc=-1
#                for xc in range(pos1[0],pos2[0]+x_inc,x_inc):
#                    #c_maze[(xc,yc)]='X'
#                    m_bdry[(xc,yc)]=1
#
#
#m_bdry=[m for m in m_bdry.keys()]
#
#m_maze={}
#for x in range(x_MIN,x_MAX+1):
#    for y in range(y_MIN,y_MAX+1):
#        m_maze[(x,y)]='.'
#for m in m_bdry:
#    m_maze[m]='X'
#
#cLine=''
#for y in range(y_MIN,y_MAX+1):
#    for x in range(x_MIN,x_MAX+1):
#        cLine += m_maze[(x,y)]
#    cLine +='\n'
#print(cLine)
#exit()

X_POS=[p[0] for p in n_pos]
Y_POS=[p[1] for p in n_pos]
X_POS.sort()
Y_POS.sort()

x_MIN= X_POS[0]
x_MAX= X_POS[-1]
y_MIN= Y_POS[0]
y_MAX= Y_POS[-1]

print('x_MIN:',x_MIN)
print('x_MAX:',x_MAX)
print('y_MIN:',y_MIN)
print('y_MAX:',y_MAX)



# iterate thought the "points of boundary" list (assuming they are
# contiguous i.e. they are traversed the same order as their order
# in the boundary polyline
# It can be assumed from the sample that it is traversed in a 
# counterclockwise direction.
# That means, for a given point to lie inside the polygon, we can
# iterate over the lines that constitutes the boundary and the check
# whether it is :
# SOUTH of line : if line goes EAST - WEST
# NORTH of line : if line goes WEST - EAST
# WEST  of line : if line goes NORTH - SOUTH
# NORTH of line : if line goes SOUTH - NORTH
# This can be treated as mapping of line to INSIDE-Direction w.r.t. Line
#
from enum import Enum
class DIRECTION(Enum):
    North = 0
    East  = 1
    South = 2
    West  = 3

def goes_east_to_west(line):
    beg=line[0]
    end=line[1]
    is_horz = beg[1] == end[1]
    if is_horz:
        if beg[0] > end[0]:
            return True
    return False

def goes_west_to_east(line):
    beg=line[0]
    end=line[1]
    is_horz = beg[1] == end[1]
    if is_horz:
        if beg[0] < end[0]:
            return True
    return False

def goes_south_to_north(line):
    beg=line[0]
    end=line[1]
    is_horz = beg[0] == end[0]
    return beg[0] == end[0] and beg[1] > end[1]

def goes_north_to_south(line):
    beg=line[0]
    end=line[1]
    return beg[0] == end[0] and beg[1] < end[1]

def get_mid_point_of_line(line00):
    pt1=line00[0]
    pt2=line00[1]
    begX=min(pt1[0],pt2[0])
    endX=max(pt1[0],pt2[0])
    begY=min(pt1[1],pt2[1])
    endY=max(pt1[1],pt2[1])
    return ((endX-begX)/2,(endY-begY)/2)

# create the list of boundary-lines and create a dictionary
# mapping line to the INSIDE-direction w.r.t. this line
m_inside_line_dict={}
m_bdry_midpoints={}
for idx1,bp1 in enumerate(n_pos):
    idx2 = idx1 + 1
    if idx2 == len(n_pos):
        idx2=0
    elif idx2 > len(n_pos):
        print("BAD IDX2",idx2)
        exit()
    bp2 = n_pos[idx2]
    #print("Adding line from",bp1,"to",bp2)
    line = (bp1, bp2)
    m_bdry_midpoints[line]=get_mid_point_of_line(line)
    if goes_east_to_west(line):
        m_inside_line_dict[line]=DIRECTION.North
    elif goes_west_to_east(line):
        m_inside_line_dict[line]=DIRECTION.South
    elif goes_north_to_south(line):
        m_inside_line_dict[line]=DIRECTION.West
    elif goes_south_to_north(line):
        m_inside_line_dict[line]=DIRECTION.East
    else:
        print("BAD LINE", line)
        exit()


def on_the_line(pt,pLine):
    is_on_x_axis = False
    is_on_y_axis = False
    beg=pLine[0]
    end=pLine[1]
    tmp=beg
    if pt[0]== beg[0] and beg[0]==end[0]:
        if beg[1]>end[1]:# swap beg and end
            beg=end
            end=tmp
        #is_on_x_axis = True
        is_on_y_axis = pt[1]>=beg[1] and pt[1] <= end[1]
    elif pt[1]== beg[1] and beg[1]==end[1]:
        if beg[0]>end[0]: # swap beg and end
            beg=end
            end=tmp
        #is_on_y_axis = True
        is_on_x_axis = pt[0]>=beg[0] and pt[0] <= end[0]
    return is_on_x_axis or is_on_y_axis

def check_point_satisfies_polygon_boundary_lines(pt):
    answer=True
    str_p=''
    for k,v in m_inside_line_dict.items():
        line_element=k
        line_beg=k[0]
        line_end=k[1]
        line_dir=v
        if line_beg[0] == pt[0] and line_beg[1]==pt[1]:
            answer=True
            str_p = ":\t\tPoint" + str(pt) + "coincide with the line beg-end" + str(line_element) + '\n'
            break
        if on_the_line(pt,line_element):
            answer=True
            str_p = ":\t\tPoint" + str(pt) + " on the line" + str(line_element) + '\n'
            break
        if line_dir==DIRECTION.West:
            if line_beg[0] >= pt[0]:
                answer = answer and True
            else:
                answer = answer and False
        elif line_dir==DIRECTION.East:
            if line_beg[0] <= pt[0]:
                answer = answer and True
            else:
                answer = answer and False
        elif line_dir==DIRECTION.North:
            if line_beg[1] >= pt[1]:
                answer = answer and True
            else:
                answer = answer and False
        elif line_dir==DIRECTION.South:
            if line_beg[1] <= pt[1]:
                answer = answer and True
            else:
                answer = answer and False
        else:
            print("BAD DIRECTION FOR LINE",line_element)
            exit()
        if answer:
            str_p += ":\t\tPoint" + str(pt) + " satisfies " + str(line_element)+ '\n'
        else:
            str_p += ":\t\tPoint" + str(pt) + " mismatches" + str(line_element)+ '\n'
    #-----------------------------------------------------------------
    if answer:
        str_p = ":\tPoint" + str(pt) + " INSIDE polygon\n" + str_p
    else:
        str_p = ":\tPoint" + str(pt) + " outside polygon\n" + str_p
    #-----------------------------------------------------------------
    print(str_p)
    return answer



def find_if_point_satisfy_line(pt,cLINE):
    line_beg=line[0]
    line_end=line[1]
    answer = False
    str_p = ''
    cLINE_DIR = m_inside_line_dict[cLINE]
    if line_beg[0] == pt[0] and line_beg[1]==pt[1]:
        answer=True
        str_p = ":\t\tPoint" + str(pt) + "coincide with the line beg-end" + str(cLINE) + '\n'
    if on_the_line(pt,cLINE):
        answer=True
        str_p = ":\t\tPoint" + str(pt) + " on the line" + str(cLINE) + '\n'
    if cLINE_DIR==DIRECTION.West:
        if line_beg[0] >= pt[0]:
            answer = True
        else:
            answer = False
    elif cLINE_DIR==DIRECTION.East:
        if line_beg[0] <= pt[0]:
            answer = True
        else:
            answer = False
    elif cLINE_DIR==DIRECTION.North:
        if line_beg[1] >= pt[1]:
            answer = True
        else:
            answer = False
    elif cLINE_DIR==DIRECTION.South:
        if line_beg[1] <= pt[1]:
            answer = True
        else:
            answer = False
    else:
        print("BAD DIRECTION FOR LINE",cLINE)
        exit()
    if answer:
        str_p += ":\t\tPoint" + str(pt) + " satisfies " + str(cLINE)
    else:
        str_p += ":\t\tPoint" + str(pt) + " mismatches" + str(cLINE)
    print(str_p)
    return answer

def get_sq_dist_bw_pts(point1,point2):
    r1 = point1[0]-point2[0]
    r2 = point1[1]-point2[1]
    return r1*r1 + r2*r2 

def find_closest_boundary_line_to_point(pt):
    
    sort_d = {get_sq_dist_bw_pts(pt,md):line for line,md in m_bdry_midpoints.items()}
    sort_d = dict(sorted(sort_d.items()))
    top_k=[k for idx,k in enumerate(sort_d.keys()) if idx==0][0]
    shortest_line = sort_d[top_k]
    #shortest_dist=-1
    #shortest_line=((-1,-1),(-1,-1))
    #for line in m_bdry_midpoints:
    #    midP = m_bdry_midpoints[line]
    #    
    #    if shortest_dist==-1 or shortest_dist < dist:
    #        shortest_dist = dist
    #        shortest_line = line
    return shortest_line

# create a line (sampled points) from point1 to point2
# and then try to see if the line (all sampled points)
# completely inside the polygon or NOT
def check_points_are_inside_polygon(pt1,pt2):
    # use the formula of line : y = m*x + c
    # where:
    # m : slope
    # c : constant
    m_slope=(pt2[1]-pt1[1])/(pt2[0]-pt1[0])
    m_const=m_slope*(0-pt1[0]) + pt1[1]
    print(":\tChecking for points:",pt1,pt2,"slope:",m_slope,"const:",m_const)
    #inc = (pt2[0] - pt1[0])/n_samples
    inc = 0.25
    if pt2[0] < pt1[0]:
        inc = -1*inc
    n_parts = int((pt2[0]-pt1[0])/inc)+1
    is_ins = False
    idx = 0
    str_p=''
    while idx < n_parts:
        x = pt1[0] + idx*inc
        if inc >0 and x > pt2[0] or inc < 0  and x < pt2[0]:
            x=p2[0]
        y = m_slope*x + m_const
        p_xy = (x,y)
        # Find the closest line to the point just created
        p_line = find_closest_boundary_line_to_point(p_xy)
        is_ins = find_if_point_satisfy_line(p_xy, p_line)
        #-----------------------------------------------------------------
        if is_ins:
            str_p += ":\n\tPoint " + str(p_xy) + " accepted by line" + str(p_line)
        else:
            str_p += ":\n\tPoint " + str(p_xy) + " rejected by line" + str(p_line)
        #-----------------------------------------------------------------
        if not is_ins:
            break
        idx += 1
    print(str_p)
    return is_ins

def get_str_from_pos(pos):
    return str(pos[0]) + ',' + str(pos[1])


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

dict_p_area={}
areaB=0
pos_1=(-1,-1)
pos_2=(-1,-1)
opp_1=(-1,-1)
opp_2=(-1,-1)
#for idx1 in range(0, len(n_lines)):
for idx1,p1 in enumerate(n_pos):
    for idx2 in range(idx1+1, len(n_pos)+1):
        # handle the last index case
        if idx2>=len(n_pos):
            break #pass
        # General Case
        p2 = n_pos[idx2]
        if p1[0]==p2[0] or p1[1]==p2[1]:
            continue
        print("processing",p1,"and",p2)
        # GEt the opposite points
        o1 = (p1[0],p2[1])
        o2 = (p2[0],p1[1])
        a12 = get_area_from_pair([p1,p2])
        #if is_inside_o1 and is_inside_o2:
        if check_points_are_inside_polygon(p1,p2) and check_points_are_inside_polygon(o1,o2):
            if areaB < a12:
                areaB = a12
                pos_1=p1
                pos_2=p2
                opp_1=o1
                opp_2=o2
        print("\t:Till now biggest area:", a12)
        dict_p_area[(p1,p2)]=a12

sorted_area = {k: v for k, v in sorted(dict_p_area.items(), key=lambda item: item[1], reverse=True)}
print("SORTNG DONE!!")
#top_key = [k for idx,k in enumerate(sorted_area.keys()) if idx==0][0]

#for poskey,valarea in sorted_area.items():
#    print("\tFor points:", poskey,"Area:",valarea)

print("Points:", pos_1,pos_2,opp_1,opp_2, " Largetst Area:", areaB)
