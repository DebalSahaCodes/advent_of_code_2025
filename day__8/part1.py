fH=open("sample.txt",'r')
f_lines=fH.readlines()
fH.close()

n_lines=[]
for line in f_lines:
    if line[-1:]=='\n':
        line=line[:-1]
    n_lines.append(line)


dict_dist={}

def get_posList_from_line(line):
    pos_list=[]
    p=line.split(',')
    for str1 in p:
        #print("\t:adding",int(str1))
        pos_list.append(int(str1))
    return pos_list

def get_dist2_from_pos12(pos1,pos2):
    dist2=0
    for i in range(0,3):
        val = pos2[i] - pos1[i]
        dist2+= val*val
    return dist2

m_pair_done=[]

def add_to_pair_done(l1,l2):
    str_p = l1+" and " +l2
    m_pair_done.append(str_p)
    return str_p
    

def is_pair_not_done(l1,l2):
    res1 = l1+" and " +l2
    res2 = l2+" and " +l1
    return res1 not in m_pair_done and res2 not in m_pair_done

for line1 in n_lines:
    p1 = get_posList_from_line(line1)
    for line2 in n_lines:
        if line1 != line2 and is_pair_not_done(line1,line2):
            str_p=add_to_pair_done(line1,line2)
            #print("processing",line1,"and",line2)
            p2 = get_posList_from_line(line2)
            d12 = get_dist2_from_pos12(p1,p2)
            if d12 not in dict_dist.keys():
                dict_dist[d12]=[]
            dict_dist[d12].append((p1,p2))

dict_dist = dict(sorted(dict_dist.items()))

#for k,v in dict_dist.items():
#    print(k,":",v)
#exit()


def are_same(prs1,prs2):
    #print("\t\t:comparing",prs1,prs2)
    res0 = prs1[0]==prs2[0]
    res1 = prs1[1]==prs2[1]
    res2 = prs1[2]==prs2[2]
    return res0 and res1 and res2



final_dict={}
new_key=0

def get_new_key():
    lst_k=list(final_dict.keys())
    if not lst_k:
        return 1
    else:
        return list(final_dict.keys())[-1] + 1

def is_found_in_v(v,pos):
    res=0
    for val in v:
        if are_same(val,pos):
            #print("\t\t:found..breaking")
            res=1
            break
    return res

def add_in_final_dict(val_p):
    #done1or2=0
    key_p0=-1
    key_p1=-1
    circuits_made = 0
    #----------
    for k,vals in final_dict.items():
        for v in vals:
            #print("\t:comparing",v,val_p[0])
            if are_same(v,val_p[0]):
                key_p0=k
            #print("\t:comparing",v,val_p[1])
            if are_same(v,val_p[1]):
                key_p1=k
            if -1!=key_p0 and -1!=key_p1:
                break
    #----------
    #----------
    if -1!=key_p0 and -1==key_p1: #0 exists; only add 1
        final_dict[key_p0].append(val_p[1])
        print("\tfound existing:",val_p[0],"adding to key:",key_p0,val_p[1],"to inc. len to", len(final_dict[key_p0]))
    elif -1==key_p0 and -1!=key_p1: #1 exists; only add 0
        final_dict[key_p1].append(val_p[0])
        print("\tfound existing:",val_p[1],"adding to key:",key_p1,val_p[0],"to inc. len to", len(final_dict[key_p1]))
    elif -1==key_p0 and -1==key_p1:
        lst=[]
        lst.append(val_p[0])
        lst.append(val_p[1])
        nKEy = get_new_key()
        final_dict[nKEy]=lst
        print("\t:adding new to key:",nKEy,val_p[1])
        print("\t:adding new to key:",nKEy,val_p[0])
        circuits_made += 1
    else:
        print("\t:already added so skipping")
        print("\t\t:",val_p[0])
        print("\t\t:",val_p[1])
    return circuits_made



tot_circuits_made=0
max_circuits=10

for _,values in dict_dist.items():
    for vals in values:
        if tot_circuits_made > max_circuits:
            break
        print("processing",vals)
        circuits_made = add_in_final_dict(vals)
        tot_circuits_made += circuits_made
        print("circuits:",tot_circuits_made)


for k,v in final_dict.items():
    print("\nTotal Values in key:",k,len(v))
    #print(v)

n_sizes=[]

for k,v in final_dict.items():
    n_sizes.append(len(v))

n_sizes.sort(reverse=True)

s_sum=1
n_idx=0
for n_idx,lenLOC in enumerate(n_sizes):
    if n_idx>   2:
        break
    print("Multiplying",lenLOC)
    s_sum*=lenLOC

print("RESULT:",s_sum)
