## Moshe Barazani
## Date: 03-05-2020

def writeScore2File(filename ,txtStr):
    fw = ""
    try:
        fw = open(filename, "w+")
        fw.writelines(txtStr)
        fw.close()
    except:
        print("cannot open file")
        exit(1)


def createGamerScoreTeplate(gamerName, gamerScore):
    print(gamerScore)

    defaultname="dGamer"
    defaultscore=0
    scoreHtml=""

    if (gamerName == ""):
        gamerName=defaultname
    if (gamerScore == "" or gamerScore == None or gamerScore == 0):
        gamerScore=defaultscore

    gamerScore = sumScore(int(gamerScore))

    scoreHtml = "<html> \n \
        <head> \n \
        <title>Scores Game</title> \n \
        </head> \n \
        <body> \n \
        <h1>Hello {GAMERNAME}</h1> \n \
        <h2>Your score is <div id='score'>{SCORE}</div></h2> \n \
        </body> \n \
        </html>\n"
    scoreHtml=scoreHtml.format(GAMERNAME=gamerName, SCORE=gamerScore)
    return scoreHtml


def sumScore(gamerScore):
    if (gamerScore != 2000):
        points_of_winning = ((gamerScore*3) + 5)
    else:
        points_of_winning = 0
    return points_of_winning