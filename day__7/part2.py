from enum import Enum

SPLITTER='^'
START='S'

def update_grid_dict_with_splitters(grid_dict,maxCOL,maxROW):
    #line=grid_dict[
    for r in range(maxROW+1):
        r_dict={}
        for c in range(maxCOL+1):
            char=grid_dict[GridPos(c,r).to_str()]
            if r>0:
                o_char=grid_dict[GridPos(c,r-1).to_str()]
            else:
                o_char=''
            if o_char=='|' or o_char=='S':
                #print("checking o_char : \"",o_char,"\"")
                if char=='^':
                    r_dict[(c-1,r)]='|'
                    r_dict[(c+1,r)]='|'
                else:
                    r_dict[(c,r)]='|'
        if len(r_dict.keys())>0:
            #print("update the current maze row")
            pass
        for nc in r_dict.keys():
            grid_dict[str(nc[0])+','+str(nc[1])]='|'



class Dircn(Enum):
    U=-1
    N=0
    E=1
    S=2
    W=3

class GridPos:
    m_x=-1
    m_y=-1
    def __init__(self, x:int, y:int):
        self.m_x=x
        self.m_y=y
    def to_str(self):
        return str(self.m_x) + ',' + str(self.m_y)
    def find_first(self):
        return m_x
    def to_the(self,d:Dircn):
        if d==Dircn.N:
            return GridPos(self.m_x, self.m_y-1)
        elif d==Dircn.E:
            return GridPos(self.m_x+1, self.m_y)
        elif d==Dircn.S:
            return GridPos(self.m_x, self.m_y+1)
        elif d==Dircn.W:
            return GridPos(self.m_x-1, self.m_y)
        else:
            print("BAD POS SENT")
            exit()

def is_in_pos_list(p:GridPos, lst):
    result=0
    for pos in lst:
        if pos.m_x==p.m_x and pos.m_y==p.m_y:
            return 1
    return result


def print_grid_dict(gridD, maxX, maxY):
    idx=0
    str_l=""
    for k in gridD.keys():
        for c in gridD[k]:
            str_l += c
            if idx>1 and idx%maxY==0:
                print(str_l+"\n")
                str_l=""
            idx+=1 


def get_pos_from_str(str_r) -> GridPos:
    str_p=str_r.split(',')
    return GridPos(int(str_p[0]),int(str_p[1]))


class Grid:
    m_dict_pos_v_char={} #dict of GridPos vs CHAR
    m_maxX=-1
    m_maxY=-1
    def __init__(self, gG:dict, mX, mY):
        self.m_dict_pos_v_char=gG
        self.m_maxX=mX
        self.m_maxY=mY
        #print("Given grid:")
        #print_grid_dict(self.m_dict_pos_v_char, self.m_maxX, self.m_maxY)
    def positions_of(self, g_char):
        pos_result = []
        for kStr,vChar in self.m_dict_pos_v_char.items():
            if vChar==g_char:
                kPos = get_pos_from_str(kStr)
                pos_result.append(kPos)
        return pos_result
    def contains_position(self, pos:GridPos):
        result=0
        for k_str,_ in self.m_dict_pos_v_char.items():
            #print("\t:checking",k.to_str())
            k=get_pos_from_str(k_str)
            if k.m_x==pos.m_x and k.m_y==pos.m_y:
                #print("\t:matched",pos.to_str())
                return 1
        return result

class PathCounter:
    m_memo={}
    m_grid=Grid
    m_splitters=[] #list of GridPos
    m_start=GridPos
    
    def __init__(self, g_grid):
        self.m_start     = g_grid.positions_of(START)[0]
        self.m_grid      = g_grid
        self.m_splitters = g_grid.positions_of(SPLITTER)
        
    def count_paths(self):
        #print("Calling from start->",self.m_start.to_str())
        return self.memoized_count_from(self.m_start)
        
    def memoized_count_from(self, p:GridPos):
        #print(":\t processing pos",p.to_str())
        p_str = p.to_str()
        if p_str in self.m_memo.keys():
            return self.m_memo[p_str]
        #if not found in memoized results then search new
        result=-1
        if not self.m_grid.contains_position(p):
            #print("not in grid",p.to_str())
            result = 1;
        elif is_in_pos_list(p,self.m_splitters):
            result = self.memoized_count_from(p.to_the(Dircn.W))
            result+= self.memoized_count_from(p.to_the(Dircn.E))
        else:
            result = self.memoized_count_from(p.to_the(Dircn.S))
        self.m_memo[p.to_str()]=result
        return result

def file_to_grid(file_path):
    fH=open(file_path)
    fLines=fH.readlines()
    fH.close()
    # remove the new-line characters
    mLines=[]
    for line in fLines:
        if line[-1:]=='\n':
            line=line[:-1]
        mLines.append(line)
    iX=-1
    iY=-1
    iG={}
    for mLine in mLines:
        iX=-1 # re-initialize X for each iter
        iY+=1 # increment Y in outer-loop
        for c in mLine:
            iX+=1 # increment X in inner loop
            #print("adding",c,"at",iX,iY)
            iG[GridPos(iX,iY).to_str()]=c
            if c=='S':
                print("position of 'S' is",iX,",",iY)
    print("Grid nCOLS:",iX)
    print("Grid nROWS:",iY)
    return iG,iX,iY



if __name__=='__main__':
    # instantiate Grid class
    #file_path = "sample.txt"
    file_path = "puzzle.txt"
    
    # create a grid - dict of position to char mapping
    c_grid_dict,g_maxX, g_maxY = file_to_grid(file_path)
    
    # solve for part 1 and insert splitters to grid
    update_grid_dict_with_splitters(c_grid_dict,g_maxX,g_maxY)

    # create Grid instance using the 
    g_Grid = Grid(c_grid_dict, g_maxX, g_maxY)
    g_Paths = PathCounter(g_Grid)
    print("TOT PATHS:", g_Paths.count_paths())
