fH=open('puzzle.txt')
#fH=open('sample.txt')
lines=fH.readlines()
fH.close()


maze={}
idxROW=-1
idxCOL=-1

for line in lines:
    idxROW += 1
    if line[:-1]=='\n':
        line=line[-1:]
    idxCOL=-1
    for c in line:
        idxCOL += 1
        maze[(idxROW,idxCOL)]=c
maxROW=idxROW
maxCOL=idxCOL

#for r in range(maxROW):
#    str_r=""
#    for c in range(maxCOL):
#        str_r += maze[(r,c)]
#    print(str_r)

print("maxCOL:",maxCOL)
print("maxROW:",maxROW)


n_splits=0
for r in range(maxROW+1):
    r_dict={}
    if 'S' in lines[r]:
        continue
    for c in range(maxCOL+1):
        char=maze[(r,c)]
        o_char=maze[(r-1,c)]
        if o_char=='|' or o_char=='S':
            print("checking o_char : \"",o_char,"\"")
            if char=='^':
                n_splits+=1
                r_dict[(r,c-1)]='|'
                r_dict[(r,c+1)]='|'
            else:
                r_dict[(r,c)]='|'
    if len(r_dict.keys())>0:
        print("update the current maze row")
    for nc in r_dict.keys():
        maze[nc]='|'

print("TOT:", n_splits)
