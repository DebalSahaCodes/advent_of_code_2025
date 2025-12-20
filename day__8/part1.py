
max_circuits=1000

fH=open("puzzle.txt",'r')
f_lines=fH.readlines()
fH.close()

n_lines=[]
for line in f_lines:
    if line[-1:]=='\n':
        line=line[:-1]
    n_lines.append(line)

n_totalPOS = len(n_lines)
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


#for idx1,line in enumerate(n_lines):
#    p1 = get_posList_from_line(line1)
#    idx2 = len(n_lines) - 1 - idx1
#    p2 = get_posList_from_line(line1)
#    for idx2,line2 in enumerate(n_lines):
#        if idx1 != idx2:
#            str_p=add_to_pair_done(line1,line2)
#            print("processing",line1,"and",line2)
#            p2 = get_posList_from_line(line2)
#            d12 = get_dist2_from_pos12(p1,p2)
#            if d12 not in dict_dist.keys():
#                dict_dist[d12]=[]
#            dict_dist[d12].append((p1,p2))


for idx1 in range(0, len(n_lines)):
    for idx2 in range(idx1, len(n_lines)):
        line1 = n_lines[idx1]
        line2 = n_lines[idx2]
        p1 = get_posList_from_line(line1)
        p2 = get_posList_from_line(line2)
        if idx1 != idx2:
            str_p=add_to_pair_done(line1,line2)
            print("processing",line1,"and",line2)
            p2 = get_posList_from_line(line2)
            d12 = get_dist2_from_pos12(p1,p2)
            if d12 not in dict_dist.keys():
                dict_dist[d12]=[]
            dict_dist[d12].append((p1,p2))


print("DONE.. now processing ...!!")


dict_dist = dict(sorted(dict_dist.items()))

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

#def is_found_in_v(v,pos):
#    res=0
#    for val in v:
#        if are_same(val,pos):
#            #print("\t\t:found..breaking")
#            res=1
#            break
#    return res

def find_keys_in_final_dict(val_p):
    #done1or2=0
    key_p0=-1
    key_p1=-1
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
    return key_p0,key_p1,val_p

def merge_in_final_dict(key_p0, key_p1):
    new_val0=final_dict[key_p0]
    for v in final_dict[key_p1]:
        new_val0.append(v)
    del final_dict[key_p1]



def add_in_final_dict(key_p0, key_p1, val_p, c_shortest):
    if -1!=key_p0 and -1==key_p1: #0 exists; only add 1
        final_dict[key_p0].append(val_p[1])
        print("\tfound existing:",val_p[0])
        print("\tadding to key:",key_p0,val_p[1],"to inc. len to", len(final_dict[key_p0]))
        #c_shortest += 1
    elif -1==key_p0 and -1!=key_p1: #1 exists; only add 0
        final_dict[key_p1].append(val_p[0])
        print("\tfound existing:",val_p[1])
        print("\tadding to key:",key_p1,val_p[0],"to inc. len to", len(final_dict[key_p1]))
        #c_shortest += 1
    elif -1==key_p0 and -1==key_p1:
        lst=[]
        lst.append(val_p[0])
        lst.append(val_p[1])
        nKEy = get_new_key()
        final_dict[nKEy]=lst
        print("\t:adding new to key:",nKEy,val_p[1])
        print("\t:adding new to key:",nKEy,val_p[0])
        #c_shortest += 1
    else:
        str_p_p0 = "\t:already added "
        str_p_p0 +="\n\t: " + str(val_p[0]) + " to key:" + str(key_p0)
        str_p_p0 +="\n\t: " + str(val_p[1]) + " to key:" + str(key_p1)
        if key_p0!=key_p1:
            str_p_p0 += " \n\t: so merging key " + str(key_p1) + " into " + str(key_p0)
            merge_in_final_dict(key_p0,key_p1)
            #c_shortest += 1
        else:
            str_p_p0 += " \n\t: so skipping"
        print(str_p_p0)
    c_shortest += 1
    return c_shortest


def check_if_new_circuit(key_p0, key_p1):
    is_new_circuit = 0
    is_add_circuit = 0
    if -1!=key_p0 and -1==key_p1: #0 exists; only add 1
        is_new_circuit = 0 # no new circuit
        is_add_circuit = 1
    elif -1==key_p0 and -1!=key_p1: #1 exists; only add 0
        is_new_circuit = 0 # no new circuit
        is_add_circuit = 1
    elif -1!=key_p0 and -1!=key_p1:
        is_new_circuit = 0 # no new circuit 
        is_add_circuit = 1 ## MERGE or PASS
    elif -1==key_p0 and -1==key_p1:
        is_new_circuit = 1 # YES new circuit
        is_add_circuit = 1
    else:
        is_new_circuit = 0 # no new circuit
        is_add_circuit = 0
    return is_new_circuit, is_add_circuit


def count_circuits_made():
    total_circuits=0
    print_str=""
    done_vals=[]
    for keys,vals in final_dict.items():
        total_circuits+=1
        print_str += str(len(vals)) + " + "
        for v in vals:
            done_vals.append(v)
    n_single_c = n_totalPOS - len(done_vals)
    if n_single_c>0:
        print_str += str(n_single_c)
        total_circuits += n_single_c
    return total_circuits, print_str

#def create_circuits():
#    for _,values in dict_dist.items():
#        for vals in values:
#            print("\nProcessing",vals)
#            kp0,kp1,boxP = find_keys_in_final_dict(vals)
#            is_new_k, to_add = check_if_new_circuit(kp0, kp1)
#            # count total circuits being made till now
#            # before adding the currently connected boxes
#            # to the tally of total-connected-circuits
#            p_str=""
#            if len(final_dict.keys())>0:
#                cur_circuits, p_str = count_circuits_made()
#                print("circuits:",p_str,"total:",cur_circuits)
#                f_cur_circuits = cur_circuits
#                if is_new_k:
#                    f_cur_circuits += 1
#                if f_cur_circuits < max_circuits:
#                    return
#            if to_add:
#                add_in_final_dict(kp0, kp1, boxP)
#                if p_str=="":
#                    cur_circuits, p_str = count_circuits_made()
#                    print("circuits:",p_str,"total:",cur_circuits)

def create_circuits():
    n_shortest = 0
    for _,values in dict_dist.items():
        for vals in values:
            print("\nProcessing",vals)
            kp0,kp1,boxP = find_keys_in_final_dict(vals)
            is_new_k, to_add = check_if_new_circuit(kp0, kp1)
            # count total circuits being made till now
            # before adding the currently connected boxes
            # to the tally of total-connected-circuits
            p_str=""
            if to_add:
                n_shortest = add_in_final_dict(kp0, kp1, boxP, n_shortest)
            cur_circuits, p_str = count_circuits_made()
            print("circuits:",p_str,"total:",cur_circuits)
            # check if MAX shortest Connections Already Made
            if len(final_dict.keys()) and n_shortest>=max_circuits:
                print(max_circuits, "circuits done!!")
                return


create_circuits()

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
