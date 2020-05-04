## Moshe Barazani
## Date: 03-05-2020
## filename: Score.py

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


def sumScore(gamerScore):
    if (gamerScore != LOSSING_CODE):
        points_of_winning = ((gamerScore*3) + 5)
    else:
        points_of_winning = 0
    return points_of_winning


def createGamerScoreTableBody(gameTime, gamerName, gamerScore, gameName):
    defaultname="WorldOfGames"
    defaultscore=0
    scoreHtml=""
    scoreHtmlBodyFormat = None

    if (gamerName == ""):
        gamerName=defaultname
    if (gamerScore == "" or gamerScore == None or gamerScore == 0):
        gamerScore=defaultscore

    gamerScore = sumScore(int(gamerScore))
    scoreHtmlBody = "{'gametime': '"+gameTime+"', 'gamername': '"+gamerName+"', 'game_name': '"+gameName+"', 'score': "+str(gamerScore)+"},"
    #scoreHtmlBodyFormat = scoreHtmlBody

    return scoreHtmlBody