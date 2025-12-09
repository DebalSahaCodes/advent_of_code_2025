import collections 

fH=open("puzzle.txt",'r')
lN=fH.readlines()
fH.close()

N_WANT=12

def is_in_dict(c,idx,dict_nCHR_xPOS1):
    is_there=0
    for k,v in dict_nCHR_xPOS1.items():
        if c==v and k==idx:
            is_there=1
            break
    return is_there


def get_largest(list_c, i_beg, i_end, dict_nCHR_xPOS1):
    if i_end<i_beg or i_beg<0 or i_end>len(list_c):
        print("BAD START STOP, i_beg:",i_beg," i_end:",i_end)
    elif i_beg==i_end:
        print("\t:returning same index, i_beg:",i_beg," i_end:",i_end)
        return list_c[i_beg]
    lar='0'
    l_x=0
    for idx,c in enumerate(list_c):
        if idx < i_beg:
            continue
        if int(c) > int(lar) and not is_in_dict(c,idx,dict_nCHR_xPOS1):
            lar=c
            l_x=idx
        if idx >= i_end:
            break
    return lar, l_x


def get_str_from_dict(dict_nCHR_xPOS1):
    result=""
    s_items=sorted(dict_nCHR_xPOS1.items())
    for _,v in s_items:
        result+=v
    return result


# find largest char position
# find remaining char AFTER the largest char
# if 11 then search next in RIGHT
# ELSE search next in LEFT

def get_largest_12_from_str(str_l):
    lo_x=0              # lowest position yet
    hi_x=len(str_l)-1    # highest position yet
    #--------------------------------------
    o_lx=-99
    o_lc='-'
    str_num=[]
    str_f=""
    id_s = 0
    id_e = len(str_l)
    dict_nCHR_xPOS={}

    i_iter=0

    while(len(str_f)<12):

        if len(dict_nCHR_xPOS)==0:
            id_s=0
        else:
            id_s=o_lx
        id_e=len(str_l)-(N_WANT-i_iter)
        #-----------
        print("Testing string between pos[",id_s,":",id_e,"]")
        #-----------
        # lc : largest char in string
        # lx : largest char pos in string
        #-----------
        lc,lx=get_largest(str_l, id_s, id_e, dict_nCHR_xPOS)
        #-----------
        if lc=='0':
            print("RET ZERO WITH id_s:",id_s," id_e:",id_e)
            exit()

        else:
        #-----------
            dict_nCHR_xPOS[lx]=lc
            str_f=get_str_from_dict(dict_nCHR_xPOS)
            print("\t: largest ->",lc," at", lx," forming,\""+str_f+"\"")
        #-----------

        if id_s>=id_e:
            print("REACHED MID..BREAKING...")
            break
        o_lx=lx
        o_lc=lc

        i_iter +=1
        if i_iter>60:
            exit()

    result=get_str_from_dict(dict_nCHR_xPOS)

    return result

sum=0
d_n={}
for idx,l in enumerate(lN):
    #if idx!=0:
    #   continue
    if l[-1:]=='\n':
        l=l[:-1]
    print(": For", l,"...\n")
    str_largest = get_largest_12_from_str(l)
    print(idx,": Largest:", str_largest)
    #exit()
    sum += int(str_largest)


print("Total Joltage:", sum)
