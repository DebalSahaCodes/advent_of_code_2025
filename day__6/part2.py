

lines=[]
fH=open('puzzle.txt')
#fH=open('sample.txt')
f_lines=fH.readlines()
fH.close()

max_col_count=0
for l in f_lines:
    if l[:-1]=='\n':
        l=l[-1:]
    if len(l) > max_col_count:
        max_col_count=len(l)
    lines.append(l)


def all_spaces(s_str):
    is_all=len(s_str)>0
    for c in s_str:
        is_all = is_all and (c == ' ' or c=='\n')
    return is_all



n_rows=len(lines)
n_IDX_without_OP=n_rows-2
# Extact numbers
n_cols=0
l_str=[]
n_str=[]
num_str=""
for col_idx in range(0, max_col_count):
    count_space=0
    col_str=""
    for l_IDX in range(0, len(lines)-1):
        curr_line = lines[l_IDX]
        # check if col-index is not exceeding current line length
        if col_idx <= len(curr_line)-1:
            #if col_idx < 0 or col_idx>len(line)-1:
            #    print("BAD col_idx", col_idx,"for line",line)
            if ' ' == curr_line[col_idx]:
                count_space+=1
            # add characters including spaces
            col_str += curr_line[col_idx]
            # if all spaces are added then discard
            if all_spaces(col_str):
                col_str=""
    if count_space < n_rows:
        str_P = "\t:After space_count:" + str(count_space)
        if col_str:
            str_P += " adding string:" + col_str
            l_str.append(col_str)
        else:
            str_P += " blank !!!"
        print(str_P)
    if count_space >= n_rows-1 or col_idx >= max_col_count-2:
        if l_str:
            print("adding :", l_str)
            n_str.append(l_str)
        l_str=[]


# extract operators
n_operators=[]
idx=0
for c in lines[-1:][0]:
    if c!=' ' and c!='\n':
        idx+=1
        n_operators.append(c)
        print("op-",idx," :", c)

for num in n_str:
    print("num:",num)


#print("op line:",lines[-1:][0])
#op_line = lines[-1:][0]

#for op_idx,op in enumerate(n_operators):
#exit()

total_sum=0

for opIDX,lst_operands in enumerate(n_str):
    c_operator = n_operators[opIDX]
    is_mul = 0
    if '*' in c_operator:
        is_mul=1
    if '*' in c_operator and '+' in c_operator:
        print("BAD OP STR:",c_operator)
        exit()
    op_result=0
    if is_mul:
        op_result=1
    for c_operand in lst_operands:
        if is_mul:
            op_result *= int(c_operand)
        else:
            op_result += int(c_operand)
    print("From col-",opIDX," :",op_result)
    total_sum += op_result

print("TOT:", total_sum)
