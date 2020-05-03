## Moshe Barazani
## Date: 03-05-2020
from Utils import *


def writeScore2File(filename ,txtStr, cmnd):
    fw = ""
    if (cmnd == "write"):
        cmnd = "w+"
    if (cmnd == "append"):
        cmnd = "a+"
    try:
        fw = open(filename, cmnd)
        fw.writelines(txtStr)
        fw.close()
    except:
        print("cannot open file")
        exit(1)


def createGamerScoreTableHeader():
    scoreHtmlHeader = "<html> \n \
            <head> \n \
            <title>Scores Game</title> \n \
            </head> \n \
            <body> \n"
    return scoreHtmlHeader

def createGamerScoreTableFooter():
    scoreHtmlFooter = "</body></html>\n"
    return scoreHtmlFooter


def createGamerScoreTableBody(gamerName, gamerScore, gameName):
    defaultname="WorldOfGames"
    defaultscore=0
    scoreHtml=""
    scoreHtmlBodyFormat = None

    if (gamerName == ""):
        gamerName=defaultname
    if (gamerScore == "" or gamerScore == None or gamerScore == 0):
        gamerScore=defaultscore

    gamerScore = sumScore(int(gamerScore))

    scoreHtmlBody = "<h2>Player: {GAMERNAME} | GameName: {GAME_NAME} | Score: {SCORE}</h2> \n"
    scoreHtmlBodyFormat = scoreHtmlBody.format(GAMERNAME=gamerName, GAME_NAME=gameName, SCORE=gamerScore)
#    scoreHtmlBodyFormat = createGamerScoreTableFooter() + scoreHtmlBodyFormat

    return scoreHtmlBodyFormat


def sumScore(gamerScore):
    if (gamerScore != LOSSING_CODE):
        points_of_winning = ((gamerScore*3) + 5)
    else:
        points_of_winning = 0
    return points_of_winning