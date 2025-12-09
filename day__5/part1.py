

fH=open("puzzle.txt")
#fH=open("sample1.txt")
lines=fH.readlines()
fH.close()

fresh_ranges=[]
check_numbers=[]
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
        fresh_ranges.append((p1,p2))
    else:
        #print("check veg:",line)
        check_numbers.append(int(line))

available_numbers={}
for idx in check_numbers:
    available_numbers[idx]=0

#fresh_numbers={}
#for beg,end in fresh_ranges:
#    for v in range(beg,end+1):
#    fresh_numbers.add(v)

def check_if_within_range(k):
    is_good=0
    for beg,end in fresh_ranges:
        if k>=beg and k<=end:
            is_good=1
            print(k,"-is fresh becaue of ",beg,"-",end)
            break
    return is_good

count_i=0
for k,_ in available_numbers.items():
    if check_if_within_range(k):
        count_i+=1

#l_fresh=list(fresh_numbers.keys())
#for n in check_numbers:
#    if n in l_fresh:
#        print(n,"-is fresh")
#        count_i+=1


print("Tot:",count_i)
