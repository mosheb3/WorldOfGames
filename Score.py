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
    defaultname="dGamer"
    defaultscore="20"
    scoreHtml=""

    if (gamerName == ""):
        gamerName=defaultname
    if (gamerScore == ""):
        gamerScore=defaultscore

    scoreHtml = "<html> \n \
        <head> \n \
        <title>Scores Game</title> \n \
        </head> \n \
        <body> \n \
        <h1>Hello {GAMERNAME}</h1> \n \
        <h2>The score is <div id='score'>{SCORE}</div></h2> \n \
        </body> \n \
        </html>\n"
    scoreHtml=scoreHtml.format(GAMERNAME=gamerName, SCORE=gamerScore)
    return scoreHtml

#POINTS_OF_WINNING = (DIFFICULTY X 3) + 5