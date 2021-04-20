import turtle as t
import random as rand
wn=t.Screen()

fontSetting=font=("System", 20, "normal")
timer=0
counterInterval=1000
timerUp=False

flagCount=10
#-----------------------------------------------------------
wn.screensize(360,420)
boardMaker=t.Turtle()
boardMaker.hideturtle()
boardMaker.penup()
boardMaker.speed(0)


counter = t.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-150,180)
counter.pendown()

scoreKeeper=t.Turtle()
scoreKeeper.hideturtle()
scoreKeeper.penup()
scoreKeeper.goto(140,180)
scoreKeeper.pendown()

#-----------------------------------------------------------
def drawBoard():
    leghtOfBoard=320
    amountOfRuns=0
    for i in range(9):
        if amountOfRuns == 0:
            boardMaker.goto(-160,160)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 1:
            boardMaker.goto(-160,120)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 2:
            boardMaker.goto(-160,80)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 3:
            boardMaker.goto(-160,40)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 4:
            boardMaker.goto(-160,0)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 5:
            boardMaker.goto(-160,-40)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 6:
            boardMaker.goto(-160,-80)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 7:
            boardMaker.goto(-160,-120)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 8:
            boardMaker.goto(-160,-160)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1
    amountOfRuns=0
    boardMaker.right(90)
    for i in range(9):
        if amountOfRuns == 0:
            boardMaker.goto(-160,160)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 1:
            boardMaker.goto(-120,160)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 2:
            boardMaker.goto(-80,160)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 3:
            boardMaker.goto(-40,160)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 4:
            boardMaker.goto(0,160)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 5:
            boardMaker.goto(40,160)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 6:
            boardMaker.goto(80,160)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 7:
            boardMaker.goto(120,160)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

        elif amountOfRuns == 8:
            boardMaker.goto(160,160)
            boardMaker.pendown()
            boardMaker.forward(leghtOfBoard)
            boardMaker.penup()
            amountOfRuns+=1

    
    boardMaker.goto(-160,180)
    boardMaker.pendown()
    boardMaker.left(90)
    boardMaker.forward(320)
    boardMaker.left(90)
    boardMaker.forward(40)
    boardMaker.left(90)
    boardMaker.forward(320)
    boardMaker.left(90)
    boardMaker.forward(40)
    boardMaker.left(90)
    boardMaker.penup()

    boardMaker.goto(-180,240)
    boardMaker.pendown()
    boardMaker.forward(360)
    boardMaker.right(90)
    boardMaker.forward(420)
    boardMaker.right(90)
    boardMaker.forward(360)
    boardMaker.right(90)
    boardMaker.forward(420)

def updateScore():
    global flagCount
    flagCount-=1
    #print(score)
    scoreKeeper.clear()
    scoreKeeper.write((str(flagCount)),font=fontSetting)
updateScore()


def countdown():
    global timer,timerUp
    counter.clear()
    
    #if there is time left
    counter.write(str(timer),font=fontSetting)
    timer+=1
    counter.getscreen().ontimer(countdown, counterInterval)

    


drawBoard()
wn.ontimer(countdown, counterInterval)
wn.mainloop()