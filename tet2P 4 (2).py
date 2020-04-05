import turtle as t
import random as r
import time


class Brick():
    def __init__(self, player):
        self.color = r.randint(1, 6)
        self.checkP = []
        self.arraP = []
        self.player = player
        self.moveX = 0
        self.moveY = 0
        self.prsXT = 0
        self.prsYT = 0

    def goGrid(self):
        self.y = 0
        self.x = len(gridP[0][0]) // 2

    def move_X(self,grid, mx):
        global die
        if True in die :
            return
        if grid[self.y][self.x + mx] == 0 :
            grid[self.y][self.x] = 0
            self.x += mx
            grid[self.y][self.x] = self.color

    def move_Y(self, grid, my):
        global die
        if True in die :
            return
        if grid[self.y + my][self.x] == 0 :
            grid[self.y][self.x] = 0
            self.y += my
            grid[self.y][self.x] = self.color

    def press_left(self, grid):
        if self.prsXT < 1:
            self.move_X(grid, -1)
        self.moveX = -1
        self.prsXT += 1

    def release_left(self):
        if self.moveX == 1:
            return
        self.moveX = 0
        self.prsXT = 0

    def press_right(self, grid):
        if self.prsXT < 1:
            self.move_X(grid, 1)
        self.moveX = 1
        self.prsXT += 1

    def release_right(self):
        if self.moveX == -1:
            return
        self.moveX = 0
        self.prsXT = 0

    def press_down(self, grid):
        if self.prsYT < 1:
            self.move_Y(grid, 1)
        self.moveY = 1
        self.prsYT += 1

    def release_down(self):
        self.moveY = 0
        self.prsYT = 0

    def fall(self, grid):
        global die
        if True in die :
            return
        for i in range(self.y + 1, len(grid)):
            if grid[i][self.x] != 0:
                grid[self.y][self.x] = 0
                self.y = i - 1
                break

    def iniGame(self, grid):
        for i in range(len(grid)):
            grid[i][0] = 7  # 왼쪽 테두리
            grid[i][1:len(grid[0]) - 1] = [0] * (len(grid[0]) - 2)
            grid[i][len(grid[i]) - 1] = 7  # 오른쪽 테두리
        grid[len(grid) - 1][0:len(grid)] = [7] * (len(grid[0]))  # 아래쪽 테두리
        for y in range(len(grid) - 2, len(grid) - 5, -1):
            for x in range(1, len(grid[0]) - 1):
                grid[y][x] = r.randint(1, 6)
        self.y = 0
        self.x = len(gridP[0][0]) // 2

    def addRow(self, grid, num=0):
        global die
        cntZero = 0
        # 내려오는 벽돌과 쌓여있는 벽돌 사이의 공간이 추가하려는 줄의 수 보다 적을 경우.
        for i in range(self.y, len(grid)):
            if grid[i][self.x] == 0:
                cntZero += 1
        if cntZero < num:
            self.y -= num - cntZero
        for i in range(num):  # num 수 만큼 아래에 줄 추가
            grid[self.y][self.x] = 0
            tmpL = [0] * (len(grid[0]) - 2)
            for i in range(len(grid[0]) - 2):
                tmpL[i] = r.randrange(1, 7)
            # grid의 맨 윗줄이 비어있지 않은데 줄이 추가되는 경우 GameOver.
            if sum(grid[0]) != 14:
                if self.player == 1:
                    die[0] = True
                else:
                    die[1] = True
                return
            else:
                del (grid[0])
            grid.insert(len(grid) - 1, [7] + tmpL + [7])
        grid[self.y][self.x] = self.color

    def arra(self, grid):  # 떠있는 벽돌 아래로 정렬
        global block, sc
        for i in range(len(grid) - 3, -1, -1):
            # i 이상의 모든 row가 비어있으면 스킵
            if sum(map(sum, grid[:i + 1])) == 14 * (i + 1):
                break
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] != 0:
                    for k in range(len(grid) - 2, i, -1):
                        if grid[k][j] == 0:
                            grid[k][j] = grid[i][j]
                            grid[i][j] = 0
                            self.arraP.append([k, j])
                            break
        if len(self.arraP) > 0:  # 정렬된 벽돌이 있다면, pang체크
            for i in range(len(self.arraP) - 1, -1, -1):
                try:
                    ttY = self.arraP[i][0]
                    ttX = self.arraP[i][1]
                    del (self.arraP[i])
                    self.pang(ttY, ttX, grid[ttY][ttX], grid)
                except Exception as e:
                    # print(e)
                    continue
            self.arra(grid)

    def pangCount(self, pangY, pangX, ncolor, grid):  # 벽돌의 상하좌우의 색깔 확인 후, 같다면 리스트에 좌표 추가
        dy = [-1, 0, 1, 0]
        dx = [0, -1, 0, 1]
        for i in range(4):
            if grid[pangY + dy[i]][pangX + dx[i]] == ncolor and [pangY + dy[i], pangX + dx[i]] not in self.checkP:
                self.checkP.append([pangY + dy[i], pangX + dx[i]])
                self.pangCount(pangY + dy[i], pangX + dx[i], ncolor, grid)

    def pang(self, pangY, pangX, ncolor, grid):
        global brickP, gridP
        self.pangCount(pangY, pangX, ncolor, grid)
        if len(self.checkP) > 3 and ncolor != 0:  # 색이 같은 벽돌이 4개 이상일때
            draw_grid(block)
            sc.update()
            # time.sleep(0.03)
            for i in range(len(self.checkP)):  # checkP에 담았던 좌표의 색을 black(0)으로 변경
                grid[self.checkP[i][0]][self.checkP[i][1]] = 0
            if self.player == 1:
                # 플레이어1 이 (pang한 갯수 -3) 만큼 플레이어2에게 선물
                brickP[1].addRow(gridP[1], len(self.checkP) - 3)
            else:
                # 플레이어1 이 (pang한 갯수 -3) 만큼 플레이어2에게 선물
                brickP[0].addRow(gridP[0], len(self.checkP) - 3)
            self.checkP = []
            self.arra(grid)
        self.checkP = []

def draw_grid(block, over=False):
    global gridP, ghost
    block.clear()  # 벽돌이 지우면서 내려가기
    ghost.clear()
    top = 250
    left = -322
    colors = ['black', 'red', 'orange', 'blue', 'yellow', 'green', 'purple', 'white']
    for i in range(2) :
        for y in range(len(gridP[0])):
            for x in range(len(gridP[0][0])):
                if gridP[i][y][x] == 0 :
                    continue
                sc_x = left + 400*i + (x * 22)
                sc_y = top - (y * 22)
                block.color(colors[gridP[i][y][x]])
                block.goto(sc_x, sc_y)
                block.stamp()
        if not over:  # 게임오버 상황이 아닌 경우
            block.color(colors[brickPP[i][1].color])  # 다음에 나올 벽돌을 화면에 표시
            block.goto(-374+400*i, 200)
            block.stamp()
            # 벽돌이 착지하게 될 곳을 ghost로 표지
            for j in range(len(gridP[0]) - 2, brickP[i].y + 1, -1):
                if gridP[i][j][brickP[i].x] == 0:
                    ghost.color(colors[brickP[i].color])
                    ghost.goto(left + 400*i + (brickP[i].x * 22), top - (j * 22))
                    ghost.stamp()
                    break
        block.goto(450, 400)
        ghost.goto(450, 400)


def gameOver(block, sc):
    global gridP, die, cond
    gridDie = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    gridWin = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]
    for i in range(len(gridP[0])):  # 게임 오버시 Win, Die 위로 올라오기
        for j in range(2) :
            del (gridP[j][0])
            if die[j] :
                gridP[j].append(gridDie[i])
            else :
                gridP[j].append(gridWin[i])
        draw_grid(block, True)
        sc.update()
    rmT = 0
    pen.clear()
    pen.goto(-180, 250)
    pen.write("GAME OVER", font=('courier', 50, 'normal'))
    pen.goto(-100, -320)
    pen.write("press R to restart", font=('courier', 15, 'normal'))
    while True:  # 깜빡깜빡
        if rmT % 2 == 1:
            for i in range(2) :
                if die[i] :
                    gridP[i] = gridDie.copy()
                else :
                    gridP[i] = gridWin.copy()
            if cond:  # r을 입력받으면 메인으로 return
                gridP[0] = gridWin.copy()  # grid가 달라지게 설정
                gridP[1] = gridDie.copy()
                die[0] = False
                die[1] = False
                cond = False
                printBG()
                return
        else:
            gridP[0] = [[0] * 14 for _ in range(25)]
            gridP[1] = [[0] * 14 for _ in range(25)]
        draw_grid(block, True)
        sc.update()
        time.sleep(0.25)
        rmT += 1


def swCond():
    global cond, die
    if True in die:
        cond = True

def pause():  # 게임 일시정지
    global sc, pen, conp
    if True in die :
        return
    if conp == False:
        conp = True
        pen.up()
        pen.clear()
        pen.goto(-80, 270)
        pen.write("PAUSE", font=('courier', 50))
        while True:
            sc.update()
            if conp == False:  # pause 상태에서 p를 누를 경우 메인으로 return
                printBG()
                return
    else:
        conp = False
        return

def printBG():
    pen.clear()
    pen.goto(-60, 290)
    pen.write("Block Game", font=('courier', 20, 'normal'))


if __name__ == "__main__":
    sc = t.Screen()
    sc.tracer(False)
    sc.bgcolor("black")
    sc.setup(width=800, height=700)

    grid1 = [[0] * 14 for _ in range(25)]
    grid2 = [[0] * 14 for _ in range(25)]


    brickPP = []
    for j in range(2) :
        tmpL = []
        for i in range(3):  # 다음에 나올 벽돌을 미리 준비
            b1 = Brick(j+1)
            tmpL.append(b1)
        brickPP.append(tmpL)

    block = t.Turtle()
    block.penup()
    block.speed(0)
    block.shape("square")
    block.color("red")
    block.setundobuffer(None)
    block.goto(-200, 200)

    ghost = t.Turtle() # ghost모양 생성
    ghost.penup()
    ghost.speed(0)
    sc.register_shape("ghost", ((-5, -3), (-5, 3), (5, 0)))
    ghost.shape("ghost")
    ghost.color("white")
    ghost.setundobuffer(None)
    ghost.goto(800, 700)

    pen = t.Turtle()
    pen.ht()
    pen.penup()
    pen.color("white")
    printBG()

    gridP = [grid1, grid2]
    brickP = [brickPP[0][0], brickPP[1][0]]
    for i in range(2) :
        brickP[i].goGrid()
        brickP[i].iniGame(gridP[i])
        gridP[i][brickP[i].y][brickP[i].x] = brickP[i].color

    draw_grid(block)

    sc.onkeypress(lambda: pause(), "p")
    sc.onkeypress(lambda: swCond(), "r")
    ## 1P key
    sc.onkeypress(lambda: brickP[0].press_left(gridP[0]), "j")
    sc.onkeyrelease(lambda: brickP[0].release_left(), "j")
    sc.onkeypress(lambda: brickP[0].press_right(gridP[0]), "l")
    sc.onkeyrelease(lambda: brickP[0].release_right(), "l")
    sc.onkeypress(lambda: brickP[0].press_down(gridP[0]), "k")
    sc.onkeyrelease(lambda: brickP[0].release_down(), "k")
    sc.onkeypress(lambda: brickP[0].fall(gridP[0]), "a")

    ## 2P key
    sc.onkeypress(lambda: brickP[1].press_left(gridP[1]), "4")
    sc.onkeyrelease(lambda: brickP[1].release_left(), "4")
    sc.onkeypress(lambda: brickP[1].press_right(gridP[1]), "6")
    sc.onkeyrelease(lambda: brickP[1].release_right(), "6")
    sc.onkeypress(lambda: brickP[1].press_down(gridP[1]), "5")
    sc.onkeyrelease(lambda: brickP[1].release_down(), "5")
    sc.onkeypress(lambda: brickP[1].fall(gridP[1]), "0")
    sc.listen()

    downT = [0,0]
    die = [False,False]
    cond = False
    conp = False

    while True:
        startT = time.time()
        for i in range(2) :
            if downT[i] >= 20:  # 벽돌이 내려오는 속도 조절
                brickP[i].move_Y(gridP[i], 1)
                downT[i] = 0
            if gridP[i][brickP[i].y+1][brickP[i].x] != 0 :
                tmpC1 = brickP[i].color
                gridP[i][brickP[i].y][brickP[i].x] = tmpC1 # 벽돌이 쌓일 경우 pang체크
                brickP[i].color = 0
                brickP[i].checkP.append([brickP[i].y, brickP[i].x])
                brickP[i].pang(brickP[i].y, brickP[i].x, tmpC1, gridP[i])
                brickPP[i][1].moveX = brickP[i].moveX
                brickPP[i][1].moveY = brickP[i].moveY
                brickPP[i][1].prsXT = brickP[i].prsXT
                brickPP[i][1].prsYT = brickP[i].prsYT
                del (brickPP[i][0])  # 벽돌 새로 생성
                b1 = Brick(i+1)
                brickPP[i].append(b1)
                brickP[i] = brickPP[i][0]
                brickP[i].goGrid()
                gridP[i][brickP[i].y][brickP[i].x] = brickP[i].color
                downT[i] = 0
            # 1P 2P 동시입력
            if brickP[i].moveX != 0 :
                if brickP[i].prsXT > 1:
                    brickP[i].move_X(gridP[i], brickP[i].moveX)
                elif brickP[i].prsXT == 1:
                    brickP[i].prsXT += 1
            if brickP[i].moveY != 0 :
                if brickP[i].prsYT > 1:
                    brickP[i].move_Y(gridP[i], brickP[i].moveY)
                elif brickP[i].prsYT == 1:
                    brickP[i].prsYT += 1

            # 새로운 벽돌이 생성되는곳이 비어있지 않으면 die
            if gridP[i][0][7] != 0:
                for k in range(len(gridP[0])):
                    if gridP[i][k][7] == 0:
                        break
                else:
                    die[i] = True
        # gameOver
        if True in die :
            gameOver(block, sc)
            for i in range(2) :
                # r을눌러 빠져나올 경우 게임초기화
                brickP[i].iniGame(gridP[i])
                gridP[i][brickP[i].y][brickP[i].x] = brickP[i].color
                downT[i]=0
        draw_grid(block)
        downT[0] += 1
        downT[1] += 1
        sc.update()
        endT = time.time()
        print(time.time()-startT)
        if(endT-startT < 0.10) :
            time.sleep(0.10-(endT-startT))


    # sc.mainloop()
