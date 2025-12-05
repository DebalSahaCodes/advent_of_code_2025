
fH=open("puzzle.txt",'r')
#fH=open("sample.txt",'r')
lN=fH.readlines()
fH.close()

def is_invalid(p:str):
    is_repeat=False
    if len(p)%2==0: # if even num of characters
        idx_n = int(len(p)/2)
        p1=p[0:idx_n]
        p2=p[idx_n:2*idx_n]
        if p1==p2:
            is_repeat=True
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
