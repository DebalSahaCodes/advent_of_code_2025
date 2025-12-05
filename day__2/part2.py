
fH=open("puzzle.txt",'r')
#fH=open("sample.txt",'r')
lN=fH.readlines()
fH.close()

def are_all_same(g_str:str):
    all_same=True
    o_c=g_str[0]
    for c in g_str:
        #print("\n\t
        all_same = all_same and c == o_c
        o_c=c
    return all_same

def create_sub_lists(str_l, subl_count:int):
    str_o=[]
    if len(str_l)%subl_count != 0: # the amount in each chunk should be same so the number to create chunks should be a multiple of the string-length
        return str_o
    i_idx=0
    while(i_idx + subl_count <= len(str_l)):
        str_c = str_l[i_idx : i_idx + subl_count]
        str_o.append(str_c)
        i_idx = i_idx + subl_count
    return str_o

def is_invalid_p2(p:str):
    is_repeat=False
    # find repeating patterns
    # Divide in smaller chunks of EQUAL sizes
    # These sizes can vary from 1 to n/2
    len_h = int(len(p)/2)
    for r in range(1,len_h+1):
        str_r=create_sub_lists(p,r)
        #print("\n\t\t: sent", str_r)
        if str_r:
            if are_all_same(str_r):
                is_repeat=True
                break
    return is_repeat

def is_invalid(p:str):
    is_repeat=False
    if len(p)%2==0: # if even num of characters
        idx_n = int(len(p)/2)
        p1=p[0:idx_n]
        p2=p[idx_n:2*idx_n]
        if p1==p2:
            is_repeat=True
    # if not dound verification here then use method-2
    if not is_repeat:
            is_repeat = is_invalid_p2(p)
    return is_repeat

r_list=[]
#lN=['11-11']
for ln in lN:
    if ln[-1:]=='\n':
        ln=ln[:-1]
    for sp in ln.split(','):
        print("\nFor range", sp)
        pt=sp.split('-')
        pt_s=int(pt[0])
        pt_e=int(pt[1])
        for pt_n in range(pt_s,pt_e+1):
            p=str(pt_n)
            str_print = "\n\t:Checking " + p
            if is_invalid(p):
                r_list.append(pt_n)
                str_print += ": INVALID , adding..."
            else:
                str_print += ": VALID"
            #print(str_print)

sum=0
for i_num in r_list:
    sum+=i_num

print("Sum of invalids: ", sum)
