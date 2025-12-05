
fH=open("puzzle.txt",'r')
lN=fH.readlines()
fH.close()

def get_largest(list_c):
    largest="11"
    for i_d in range(len(list_c)):
        c_id=list_c[i_d]
        for idx,c in enumerate(list_c):
            if idx <= i_d:
                continue
            str_c = c_id + c 
            if int(str_c) > int(largest):
                largest=str_c
    return largest

sum=0
d_n={}
for idx,l in enumerate(lN):
    if l[-1:]=='\n':
        l=l[:-1]
    str_largest = get_largest(l)
    sum += int(str_largest)
    print(idx,": LArgest:", get_largest(l))








print("Total Joltage:", sum)
