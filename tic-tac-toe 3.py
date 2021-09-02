#let's play tic-tac-toe game
#이거 괜찮은거 맞나 싶고..

board = [[' ' for x in range(3)] for y in range(3)]
x = 0
y = 0
garo1 = 0
garo2 = 0
garo3 = 0
sero1 = 0
sero2 = 0
sero3 = 0
left = 0
right = 0


#보드판 그리기
def draw_board():
    for r in range(3):
        print("  "+board[r][0]+"|  "+board[r][1]+"|  "+board[r][2])
        if(r != 2):
            print("---|---|---")

#사용자로부터 좌표값 입력받고 출력하기
def get_location():
    global garo1, garo2, garo3, sero1, sero2, sero3, left, right
    locate = True
    while locate:
        global x
        global y
        x = int(input("x 좌표를 입력하세요: "))
        y = int(input("y 좌표를 입력하세요: "))
        if board[y][x] != ' ':
            print("잘못된 위치입니다.")
            continue
        else:
            board[y][x] = 'X'
            if(x == 0 and y == 0):
                garo1 += 1
                sero1 += 1
                left += 1
            elif(x == 1 and y == 0):
                garo1 += 1
                sero2 += 1
            elif(x == 2 and y == 0):
                garo1 += 1
                sero3 += 1
                right += 1
            elif(x == 0 and y == 1):
                garo2 += 1
                sero1 += 1
            elif(x == 1 and y == 1):
                garo2 += 1
                sero2 += 1
                left += 1
                right += 1
            elif(x == 2 and y == 1):
                garo2 += 1
                sero3 += 1
            elif(x == 0 and y == 2):
                garo3 += 1
                sero1 += 1
                right += 1
            elif(x == 1 and y == 2):
                garo3 += 1
                sero2 += 1
            elif(x == 2 and y == 2):
                garo3 += 1
                sero3 += 1
                left += 1
            locate = False

#컴퓨터 위치 결정
def get_computer():
    global garo1, garo2, garo3, sero1, sero2, sero3, left, right
    done = False
    if(garo1 == 2):
        for i in range(3):
            if board[0][i] == ' ' and not done:
                board[0][i] = '0'
                garo1 += 1
                done = True
                break
            
    elif(garo2 == 2):
        for i in range(3):
            if board[1][i] == ' ' and not done:
                board[1][i] = '0'
                garo2 += 1
                done = True
                break
            
    elif(garo3 == 2):
        for i in range(3):
            if board[2][i] == ' ' and not done:
                board[2][i] = '0'
                garo3 += 1
                done = True
                break
            
    elif(sero1 == 2):
        for i in range(3):
            if board[i][0] == ' ' and not done:
                board[i][0] = '0'
                sero1 += 1
                done = True
                break
            
    elif(sero2 == 2):
        for i in range(3):
            if board[i][1] == ' ' and not done:
                board[i][1] = '0'
                sero2 += 1
                done = True
                break
            
    elif(sero3 == 2):
        for i in range(3):
            if board[i][2] == ' ' and not done:
                board[i][2] = '0'
                sero3 += 1
                done = True
                break
            
    elif(left == 2):
        for i in range(3):
            if board[i][i] == ' ' and not done:
                board[i][i] = '0'
                left += 1
                done = True
                break
    
    elif(right == 2): 
        xx = -1
        yy = 3
        for i in range(3):
            xx += 1
            yy -= 1
            if board[xx][yy] == ' ' and not done:
                board[xx][yy] = '0'
                right += 1
                done = True
                break
                
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ' and not done:
                    board[i][j] = '0'
                    done = True
                    break

def main():
    draw_board()
    for i in range(5):
        get_location()
        get_computer()
        draw_board()

main()