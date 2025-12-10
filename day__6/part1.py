
lines=[]
fH=open('puzzle.txt')
lines=fH.readlines()
fH.close()

NC=[]

for idx,line in enumerate(lines):
    if line[:-1]=='\n':
        line=line[-1:]
    pr=line.split()
    if idx<len(lines)-1:
        n_pr=[]
        for val in pr:
            n_pr.append(int(val))
        #print("adding a list of size:", len(n_pr))
        NC.append(n_pr)
    else:
        #print("adding a list of size:", len(pr))
        NC.append(pr)

print("Rows in NC:",len(NC))
#exit()

operators_row=NC[-1:][0]
print("Total num of operators:",len(operators_row),"\n\n")
#print("list op",operators_row)
N_OPERANDS=len(NC)-1
total_sum=0

#access value in each row 
for col in range(0, len(operators_row)):
    col_sum=0
    is_mul = operators_row[col]=='*'
    if is_mul:
        col_sum=1
    print("Using operator:",operators_row[col])
    for r_idx,row in enumerate(NC):
        if r_idx<N_OPERANDS:
            print("\t: operand-",col," :",row[col])
            if is_mul:
                col_sum *= row[col]
            else:
                col_sum += row[col]
    print("Adding total from col-",col," :",col_sum)
    total_sum += col_sum

print("TOT SUM:", total_sum)

#print("len(r1)",len(r1))
#print("len(r2)",len(r2))
#print("len(r3)",len(r3))
#print("len(r4)",len(r4))

