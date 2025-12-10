
fH=open("puzzle.txt")
#fH=open("sample2.txt")
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
o_beg=0
o_end=0
idx=0
for beg,end in f_sorted_set:
    if idx>0:
        if beg<=o_end and end<=o_end:
            idx+=1
            print("Skipping addition of", beg,"-",end,"because of o_beg:",o_beg,"o_end:",o_end)
            continue
        elif beg<=o_end and end>o_end:
            idx+=1
            print("Merging", beg,"-",end,"and", o_beg,"-",o_end,"to form",o_beg,"-",end)
            fresh_ranges[o_beg]=end
            o_end=end
            continue
    fresh_ranges[beg]=end
    print("added", beg,"-",end)
    o_beg=beg
    o_end=end
    idx+=1


print("POST SORT:")
for k,v in fresh_ranges.items():
    print("check range:",k,"-",v)



count_i=0
for beg,end in fresh_ranges.items():
    curr_i=end-beg+1
    print(beg,"_",end,curr_i)
    count_i += curr_i

print("Tot:",count_i)
