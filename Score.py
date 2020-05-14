## Moshe Barazani
## Date: 03-05-2020
## filename: Score.py

from Utils import *

def write_score_2_file(filename ,txtStr, cmnd):
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


def sum_score(gamer_score):
    if (gamer_score != LOSSING_CODE):
        points_of_winning = ((gamer_score*3) + 5)
    else:
        points_of_winning = 0
    return points_of_winning


def createGamerScoreTableBody(game_time, gamer_name, gamer_score, game_name):
    defaultname="WorldOfGames"
    defaultscore=0
    scoreHtml=""
    scoreHtmlBodyFormat = None

    if (gamer_name == ""):
        gamer_name=defaultname
    if (gamer_score == "" or gamer_score == None or gamer_score == 0):
        gamer_score=defaultscore

    gamer_score = sum_score(int(gamer_score))
    scoreHtmlBody = "{'gametime': '"+game_time+"', 'gamername': '"+gamer_name+"', 'game_name': '"+game_name+"', 'score': "+str(gamer_score)+"},"

    return scoreHtmlBody