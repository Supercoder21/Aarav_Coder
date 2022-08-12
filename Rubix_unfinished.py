from pytextgame import *
def colorscheme(x):
    if x == 'W':
        return WHITE
    elif x == 'Y':
        return YELLOW
    elif x == 'B':
        return BLUE
    elif x == 'O':
        return BEIGE
    elif x == 'R':
        return RED
    elif x == 'G':
        return GREEN
    else:
        return None
def raw_data(l,f):
    newl = str(l)
    newl = newl.replace('[','')
    newl = newl.replace(']','')
    newl = newl.replace(',','')
    newl = newl.replace('"','')
    newl = newl.replace("'",'')
    newl = newl.replace(' ','')
    raw2norm = ''
    if f == 1 or f == 2:
        prep = '     \n     \n     '
    else:
        prep = ''
    count = 0
    for i in newl:
        count = count+1
        activate = True
        if f != 1 and f != 2:
            if count%3 == 0:
                raw2norm = raw2norm+' '+colortext(colorscheme(i),i)+'|'
                continue
        if count%3 == 1:
            if f == 1 or f == 2:
                raw2norm = raw2norm + '\n      '
                raw2norm = raw2norm + colortext(colorscheme(i),i)
            else:
                raw2norm = raw2norm + '\n'
                raw2norm = raw2norm + colortext(colorscheme(i),i)
        else:
            raw2norm = raw2norm+' '+colortext(colorscheme(i),i)
    return raw2norm


class Cube:
    def __init__(self):
        self.top_face = [['W','W','W'],['W',"W",'W'],['W',"W",'W']]
        self.bottom_face = [['Y','Y','Y'],['Y',"Y",'Y'],['Y',"Y",'Y']]
        self.layer_1 = [['B','B','B'],['O','O','O'],['G','G','G'],['R','R','R']]
        self.layer_2 = [['B','B','B'],['O','O','O'],['G','G','G'],['R','R','R']]
        self.layer_3 = [['B','B','B'],['O','O','O'],['G','G','G'],['R','R','R']]
        self.face1=[]
        self.face2=[]
        self.face3=[]
        self.face4=[]
        self.face5=[]
        self.face6=[]
    def show(self):
        self.face1 = self.top_face
        print('Top Face')
        for i in self.top_face:
            print(i)
        self.face2 = self.bottom_face
        print('Bottom face')
        for x in self.bottom_face:
            print(x)
        print('1st Face')
        self.face3 = [self.layer_1[0],self.layer_2[0],self.layer_3[0]]
        print(self.layer_1[0])
        print(self.layer_2[0])
        print(self.layer_3[0])
        print('2nd Face from perspective of blue side')
        self.face4 = [self.layer_1[1],self.layer_2[1],self.layer_3[1]]
        print(self.layer_1[1])
        print(self.layer_2[1])
        print(self.layer_3[1])
        print('3rd Face from perspective of blue side')
        self.face5 = [self.layer_1[2],self.layer_2[2],self.layer_3[2]]
        print(self.layer_1[2])
        print(self.layer_2[2])
        print(self.layer_3[2])
        print('4th Face')
        self.face6 = [self.layer_1[3],self.layer_2[3],self.layer_3[3]]
        print(self.layer_1[3])
        print(self.layer_2[3])
        print(self.layer_3[3])
    def r(self):
        self.new_lis = []
        self.new_lis.append(self.layer_1[0][2])
        self.new_lis.append(self.layer_2[0][2])
        self.new_lis.append(self.layer_3[0][2])
        self.back_lis = []
        self.back_lis.append(self.layer_1[2][2])
        self.back_lis.append(self.layer_2[2][2])
        self.back_lis.append(self.layer_3[2][2])
        self.top_lis = []
        self.top_lis.append(self.top_face[0][2])
        self.top_lis.append(self.top_face[1][2])
        self.top_lis.append(self.top_face[2][2])
        self.bottom_lis = []
        self.bottom_lis.append(self.bottom_face[0][2])
        self.bottom_lis.append(self.bottom_face[1][2])
        self.bottom_lis.append(self.bottom_face[2][2])
        self.top_face[0][2] = self.new_lis[0]
        self.top_face[1][2] = self.new_lis[1]
        self.top_face[2][2] = self.new_lis[2]
        self.layer_1[2][2] = self.top_lis[0]
        self.layer_2[2][2] = self.top_lis[1]
        self.layer_3[2][2] = self.top_lis[2]
        self.bottom_face[0][2] = self.back_lis[0]
        self.bottom_face[1][2] = self.back_lis[1]
        self.bottom_face[2][2] = self.back_lis[2]
        self.layer_1[0][2] = self.bottom_lis[0]
        self.layer_2[0][2] = self.bottom_lis[1]
        self.layer_3[0][2] = self.bottom_lis[2]
        pop = tuple(self.layer_1[1])
        self.top = pop
        self.left = []
        self.left.append(self.layer_1[1][0])
        self.left.append(self.layer_2[1][0])
        self.left.append(self.layer_3[1][0])
        self.left.reverse()
        jop = tuple(self.layer_3[1])
        self.bottom = jop
        self.right = []
        cop = tuple(self.layer_1)
        bop = tuple(self.layer_2)
        chop = tuple(self.layer_3)
        self.right.append(cop[1][2])
        self.right.append(bop[1][2])
        self.right.append(chop[1][2])
        self.right.reverse()

        self.layer_1[1] = self.left

        self.layer_1[1][2] = self.top[0]
        self.bot = self.bottom
        self.layer_2[1][2] = self.top[1]
        self.bottom = self.bot
        self.layer_3[1][2] = self.top[2]
        self.layer_3[1] = self.right
        self.layer_3[1][0] = self.bottom[2]
        self.layer_2[1][0] = self.bottom[1]
        self.layer_1[1][0] = self.bottom[0]
    def r_prime(self):
        self.r()
        self.r()
        self.r()
    def l(self):
        self.new_lis = []
        self.new_lis.append(self.layer_1[0][0])
        self.new_lis.append(self.layer_2[0][0])
        self.new_lis.append(self.layer_3[0][0])
        self.back_lis = []
        self.back_lis.append(self.layer_1[2][0])
        self.back_lis.append(self.layer_2[2][0])
        self.back_lis.append(self.layer_3[2][0])
        self.top_lis = []
        self.top_lis.append(self.top_face[0][0])
        self.top_lis.append(self.top_face[1][0])
        self.top_lis.append(self.top_face[2][0])
        self.bottom_lis = []
        self.bottom_lis.append(self.bottom_face[0][0])
        self.bottom_lis.append(self.bottom_face[1][0])
        self.bottom_lis.append(self.bottom_face[2][0])
        self.top_face[0][0] = self.new_lis[0]
        self.top_face[1][0] = self.new_lis[1]
        self.top_face[2][0] = self.new_lis[2]
        self.layer_1[2][0] = self.top_lis[0]
        self.layer_2[2][0] = self.top_lis[1]
        self.layer_3[2][0] = self.top_lis[2]
        self.bottom_face[0][0] = self.back_lis[0]
        self.bottom_face[1][0] = self.back_lis[1]
        self.bottom_face[2][0] = self.back_lis[2]
        self.layer_1[0][0] = self.bottom_lis[0]
        self.layer_2[0][0] = self.bottom_lis[1]
        self.layer_3[0][0] = self.bottom_lis[2]
        pop = tuple(self.layer_1[3])
        self.top = pop
        self.left = []
        self.left.append(self.layer_1[3][0])
        self.left.append(self.layer_2[3][0])
        self.left.append(self.layer_3[3][0])
        self.left.reverse()
        jop = tuple(self.layer_3[3])
        self.bottom = jop
        self.right = []
        cop = tuple(self.layer_1)
        bop = tuple(self.layer_2)
        chop = tuple(self.layer_3)
        self.right.append(cop[3][2])
        self.right.append(bop[3][2])
        self.right.append(chop[3][2])
        self.right.reverse()

        self.layer_1[3] = self.left

        self.layer_1[3][2] = self.top[0]
        self.bot = self.bottom
        self.layer_2[3][2] = self.top[1]
        self.bottom = self.bot
        self.layer_3[3][2] = self.top[2]
        self.layer_3[3] = self.right
        self.layer_3[3][0] = self.bottom[2]
        self.layer_2[3][0] = self.bottom[1]
        self.layer_1[3][0] = self.bottom[0]
    def l_prime(self):
        self.l()
        self.l()
        self.l()
    def u(self):
        self.curr_1 = self.layer_1[0]
        self.curr_2 = self.layer_1[1]
        self.curr_3 = self.layer_1[2]
        self.curr_4 = self.layer_1[3]
        self.layer_1[0] = self.curr_2

        self.layer_1[3] = self.curr_1
        self.layer_1[2] = self.curr_4
        self.layer_1[1] = self.curr_3
        self.start = tuple(self.top_face[0])
        self.end = tuple(self.top_face[2])
        self.right = []
        self.left = []
        self.left.append(self.top_face[0][2])
        self.left.append(self.top_face[1][2])
        self.left.append(self.top_face[2][2])
        self.left.reverse()
        self.right.append(self.top_face[0][0])
        self.right.append(self.top_face[1][0])
        self.right.append(self.top_face[2][0])
        self.right.reverse()
        self.top_face[0] = self.right
        self.top_face[0][2] = self.start[0]
        self.top_face[1][2] = self.start[1]
        self.top_face[2][2] = self.start[2]
        self.top_face[2] = self.left
        self.top_face[2][0] = self.end[2]
        self.top_face[1][0] = self.end[1]
        self.top_face[0][0] = self.end[0]
    def u_prime(self):
        self.u()
        self.u()
        self.u()
    def f(self):
        self.top_color = self.top_face[2]
        self.bottom_color = self.bottom_face[0]
        self.right_color = []
        self.right_color.append(self.layer_1[1][0])
        self.right_color.append(self.layer_2[1][0])
        self.right_color.append(self.layer_3[1][0])
        self.left_color = []
        self.right_color.reverse()
        self.left_color.append(self.layer_1[3][2])
        self.left_color.append(self.layer_2[3][2])
        self.left_color.append(self.layer_3[3][2])
        self.left_color.reverse()
        self.top_face[2] = self.left_color
        self.layer_1[1][0] = self.top_color[0]
        self.layer_2[1][0] = self.top_color[1]
        self.layer_3[1][0] = self.top_color[2]
        self.bottom_face[0] = self.right_color
        self.layer_3[3][2] = self.bottom_color[2]
        self.layer_2[3][2] = self.bottom_color[1]
        self.layer_1[3][2] = self.bottom_color[0]
        pop = tuple(self.layer_1[0])
        self.top = pop
        self.left = []
        self.left.append(self.layer_1[0][0])
        self.left.append(self.layer_2[0][0])
        self.left.append(self.layer_3[0][0])
        self.left.reverse()
        jop = tuple(self.layer_3[0])
        self.bottom = jop
        self.right = []
        cop = tuple(self.layer_1)
        bop = tuple(self.layer_2)
        chop = tuple(self.layer_3)
        self.right.append(cop[0][2])
        self.right.append(bop[0][2])
        self.right.append(chop[0][2])
        self.right.reverse()

        self.layer_1[0] = self.left

        self.layer_1[0][2] = self.top[0]
        self.bot = self.bottom
        self.layer_2[0][2] = self.top[1]
        self.bottom = self.bot
        self.layer_3[0][2] = self.top[2]
        self.layer_3[0] = self.right
        self.layer_3[0][0] = self.bottom[2]
        self.layer_2[0][0] = self.bottom[1]
        self.layer_1[0][0] = self.bottom[0]
    def data(self):
        self.face1 = self.top_face
        self.face2 = self.bottom_face
        self.face3 = [self.layer_1[0],self.layer_2[0],self.layer_3[0]]
        self.face4 = [self.layer_1[1],self.layer_2[1],self.layer_3[1]]
        self.face5 = [self.layer_1[2],self.layer_2[2],self.layer_3[2]]
        self.face6 = [self.layer_1[3],self.layer_2[3],self.layer_3[3]]
        return {1:self.face1,2:self.face2,3:self.face3,4:self.face4,5:self.face5,6:self.face6}
class Simulator:
    def __init__(self,data):
        self.face1 = raw_data(data[1],1)
        self.face2 = raw_data(data[2],2)
        self.face3 = raw_data(data[3],3)
        self.face4 = raw_data(data[4],4)
        self.face5 = raw_data(data[5],5)
        self.face6 = raw_data(data[6],6)
    def simulate(self):
        print(self.face1)
        splt_lines = zip(self.face6.split('\n'), self.face5.split('\n'),self.face4.split('\n'),self.face3.split('\n'))
        res = '\n'.join([x + y + z + a for x, y, z, a in splt_lines])
        print(str(res))
        print(self.face2)
rubix = Cube()
rubix.r()
data = Simulator(rubix.data())
data.simulate()
