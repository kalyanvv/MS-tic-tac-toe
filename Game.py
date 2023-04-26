import pygame,sys,random,time
from pygame.locals import *


pygame.init()

BackroundColor=(255,255,255)

FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 400
initPosX=50
initPosY=100+50
isPresentPageHome=False

WINDOW = pygame.display.set_mode((WINDOW_WIDTH+450, WINDOW_HEIGHT))
pygame.display.set_caption('tic tac toe pygame')

board=[[-1 for i in range(3)] for j in range(3)]
isXTurn=True
# drawing board
def draw():
    fontObj=pygame.font.Font(None, 100)
    for i in range(3):
        for j in range(3):
            if(board[i][j]==1):
                textSufaceObj = fontObj.render('X', True, (0, 255, 197), None)
                text_rect = textSufaceObj.get_rect(center=(initPosX+100*i, initPosY+100*j))
                WINDOW.blit(textSufaceObj,text_rect)
            elif(board[i][j]==0):
                textSufaceObj = fontObj.render('O', True, "#ec008c", None)
                text_rect = textSufaceObj.get_rect(center=(initPosX+100*i, initPosY+100*j))
                WINDOW.blit(textSufaceObj,text_rect)
            else:
                pass


def instructions():
    fontObj=pygame.font.Font(None, 25)
    textSufaceObj = fontObj.render('Instructions', True, "white", None)
    WINDOW.blit(textSufaceObj,(450,80))
    fontObj=pygame.font.Font(None, 20)
    textSufaceObj = fontObj.render('• Two players take turns placing X and O symbols on a 3*3 grid.', True, "white", None)
    WINDOW.blit(textSufaceObj,(310,120))
    textSufaceObj = fontObj.render('• Goal of the game is to get three of your symbols in a row',True, "white", None)
    WINDOW.blit(textSufaceObj,(310,140))
    textSufaceObj = fontObj.render('• The first player to achieve so, Wins the game.',True, "white", None)
    WINDOW.blit(textSufaceObj,(310,160))
    textSufaceObj = fontObj.render('• Enjoy the Game :).',True, "white", None)
    WINDOW.blit(textSufaceObj,(310,180))
    fontObj=pygame.font.Font(None, 20)
    textSufaceObj = fontObj.render("• Enter 'q' to exit the Game.",True, "white", None)
    WINDOW.blit(textSufaceObj,(310,200))



# game home screen
def home():
    global isPresentPageHome
    isPresentPageHome=True
    WINDOW.fill((27, 20, 100))
    # WINDOW.fill((0,0,0))
    fontObj=pygame.font.Font(None, 30)
    textSufaceObj = fontObj.render("X's Turn" if isXTurn else "O's Turn", True, "white", None)
    WINDOW.blit(textSufaceObj,(120,30))

    pygame.draw.line(WINDOW,(0, 255, 197), (WINDOW_WIDTH / 3, 100), (WINDOW_WIDTH / 3, WINDOW_HEIGHT-20), 4)
    pygame.draw.line(WINDOW,(0, 255, 197), (WINDOW_WIDTH / 3 * 2, 100),
                 (WINDOW_WIDTH / 3 * 2, WINDOW_HEIGHT-20), 4)
    
    pygame.draw.line(WINDOW,"#ec008c", (20, 100+WINDOW_WIDTH / 3), (WINDOW_WIDTH-20,100+WINDOW_WIDTH / 3), 4)
    pygame.draw.line(WINDOW,"#ec008c", (20, 100+(WINDOW_WIDTH / 3)*2), (WINDOW_WIDTH-20,100+(WINDOW_WIDTH / 3)*2), 4)
    instructions()
    draw()


# updating board
def updateBoard(mx,my,Symbol): 
    global isXTurn
    row=-1
    col=-1
    if(my<=100):
        pass
    elif(my<=200):
        row=0
    elif(my<=300):
        row=1
    elif(my<=400):
        row=2
    
    if(mx<=100):
        col=0
    elif(mx<=200):
        col=1
    elif(mx<=300):
        col=2
    
    if(row!=-1 and col!=-1):
        if(board[col][row]==-1):
            sound = pygame.mixer.Sound("./audio1.wav")
            sound.play()
            board[col][row]=Symbol
            isXTurn=not isXTurn
        else:
            sound = pygame.mixer.Sound("./wrong.mp3")
            sound.play() 


def checkBoard():
    emptyCount=0
    for i in range(3):
        for j in range(3):
            if(board[i][j]==-1):
                emptyCount+=1
    
    if(emptyCount==0):
        return -1
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != -1:
            return board[i][0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != -1:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != -1:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != -1:
        return board[0][2]
    
    # No winner yet
    return None


def landingScreen():
    WINDOW.fill((27, 20, 100))
    sound = pygame.mixer.Sound("./start.mp3")
    sound.play(maxtime=5000,fade_ms=500)
    sound.fadeout(5000)
    image=pygame.image.load('./p2.png')
    new_size = (200, 200)
    resized_image = pygame.transform.scale(image, new_size)
    WINDOW.blit(resized_image,(50,90))
    fontObj=pygame.font.Font(None, 30)
    textSufaceObj = fontObj.render('Welcome to the Game', True, "#ec008c", None)
    text_rect = textSufaceObj.get_rect(center=(150, 330))
    WINDOW.blit(textSufaceObj,text_rect)
    textSufaceObj = fontObj.render('Loading...', True, (0, 255, 197), None)
    text_rect = textSufaceObj.get_rect(center=(150, 360))
    WINDOW.blit(textSufaceObj,text_rect)
    instructions()
    pygame.display.update()

def main():
    looping=True
    global board
    global isXTurn
    global isPresentPageHome
    landingScreen()
    time.sleep(5)
    while(looping):

        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()
            if(event.type==pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if(isPresentPageHome):
                    updateBoard(mouse_x,mouse_y,1 if isXTurn==True else 0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
           
        
        

        winStatus=checkBoard()
        if(winStatus!=None):
            isPresentPageHome=False
            WINDOW.fill((27, 20, 100))
            fontObj=pygame.font.Font(None, 30)

            if(winStatus==-1):
                sound = pygame.mixer.Sound("./audio3.mp3")
                sound.play()      
                textSufaceObj = fontObj.render('Game is a Draw', True, "white", None)
            else:
                sound = pygame.mixer.Sound("./audio2.wav")
                sound.play()
                textSufaceObj = fontObj.render('Game is won by '+("O" if winStatus==0 else "X"), True, "white", None)

            text_rect = textSufaceObj.get_rect(center=(150, 200))
            WINDOW.blit(textSufaceObj,text_rect)
            fontObj=pygame.font.Font(None, 20)
            textSufaceObj = fontObj.render("Redirecting to New Game...", True, "white", None)
            text_rect = textSufaceObj.get_rect(center=(150, 220))
            WINDOW.blit(textSufaceObj,text_rect)
            instructions()
            pygame.display.update()
            time.sleep(5)
            board=[[-1 for i in range(3)] for j in range(3)]
            isXTurn=True
            # WINDOW.fill(BackroundColor)
            home()          
        else:
            home()

        pygame.display.update()
        fpsClock.tick(60)

main()
# home()