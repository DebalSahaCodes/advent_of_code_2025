
fH=open("puzzle.txt",'r')
#fH=open("sample.txt",'r')
f_lines=fH.readlines()
fH.close()

n_lines=[]# remove '\n'
for line in f_lines:
    if line[-1:]=='\n':
        line=line[:-1]
    n_lines.append(line)

def get_posList_from_line(line):
    return [int(c) for c in line.split(',')]

def get_dist_bw_pos1_pos2(pos1,pos2):
    dist2=0
    for i in range(0,2):
        val = pos2[i] - pos1[i]
        dist2+= val*val
    return dist2

dict_dist={}

b_dist=0
b_pair=[]
b_line=[]
for idx1 in range(0, len(n_lines)):
    for idx2 in range(idx1, len(n_lines)):
        line1 = n_lines[idx1]
        line2 = n_lines[idx2]
        if idx1 != idx2:
            #print("processing",line1,"and",line2)
            p1 = get_posList_from_line(line1)
            p2 = get_posList_from_line(line2)
            d12 = get_dist_bw_pos1_pos2(p1,p2)
            #print("\t:", d12)
            if d12 > b_dist:
                b_dist=d12
                b_pair=[]
                b_pair.append(p1)
                b_pair.append(p2)
                b_line=[]
                b_line.append(line1)
                b_line.append(line2)

x=b_pair[0][0] - b_pair[1][0]
if x<0:
    x = x*-1
x = x+1
y=b_pair[0][1] - b_pair[1][1]
if y<0:
    y = y*-1
y=y+1
print("Biggest Area from ",b_line)
print('x:',x,' y:',y,' =',x*y)
