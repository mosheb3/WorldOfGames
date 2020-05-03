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

#POINTS_OF_WINNING = (DIFFICULTY X 3) + 5