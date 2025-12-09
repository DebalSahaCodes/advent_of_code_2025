
#319434630622799
#361615643045068<--too high.
fH=open("puzzle.txt")
#fH=open("sample1.txt")
lines=fH.readlines()
fH.close()


ufresh_ranges=[]
is_break=0
for line in lines:
    if line=='\n':
        is_break=1
        continue
    if line[-1:]=='\n':
        line=line[:-1]
    if not is_break:
        #print("check range:",line)
        p=line.split('-')
        p1=int(p[0])
        p2=int(p[1])
        ufresh_ranges.append((p1,p2))
    else:
        #print("check veg:",line)
        #check_numbers.append(int(line))
        break

f_sorted_set=sorted(ufresh_ranges)

fresh_ranges={}

for v1,v2 in f_sorted_set:
    fresh_ranges[v1]=v2

#print("POST SORT:")
#for k,v in fresh_ranges.items():
#    print("check range:",k,"-",v)

final_pairs=[]
#o_beg=0
#o_end=0
#for beg,end in fresh_ranges.items():
#    skip_beg=0
#    skip_end=0
#    if o_beg>0 and o_end>0:
#        if o_beg<beg and beg<o_end:
#            skip_beg=1
#        if o_end<beg:
#            skip_end=1
#    o_beg=beg
#    o_end=end

o_beg=0
o_end=0
del_k=[]
mod_k={}
for beg,end in fresh_ranges.items():
    if o_beg>0 and o_end>0 and o_beg<beg:
        str_R=""
        if beg<o_end:
            if end<=o_end:
                #print("del",beg)
                end=o_end
                pass
            else:
                str_R = "mod:" + str(o_beg)
                mod_k[o_beg]=end
            #print(str_R + " del:"+str(beg))
            del_k.append(beg)
            beg=o_beg
    o_beg=beg
    o_end=end

for k in del_k:
    del fresh_ranges[k]

for k,v in mod_k.items():
    fresh_ranges[k]=v


count_i=0
for beg,end in fresh_ranges.items():
    curr_i=end-beg+1
    print(beg,"_",end,curr_i)
    count_i += curr_i

print("Tot:",count_i)
