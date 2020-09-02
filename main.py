boarddic={
            '7':' ', '8':' ', '9':' ',
            '4':' ', '5':' ', '6':' ',
            '1':' ', '2':' ', '3':' '
        }

def board(board):
    print(board['7'], "|", board['8'], "|", board['9'])
    print("- + - + -")
    print(board['4'], "|", board['5'], "|", board['6'])
    print("- + - + -")
    print(board['1'], "|", board['2'], "|", board['3'])

#from goto import with_goto
#@with_goto


def game():

    #str(turn)
    #turn='x'
    #i=0
    global turn
    global i
    turn='x'
    i=0

    for i in range(10):
        board(boarddic)
        place=input("輸入位置")
        
        if boarddic[place] == ' ':
            boarddic[place]=turn
            recognize()
            i+=1
        else :
            print("重新輸入")
            continue#??

        if turn=='x':
            turn='O'
        else:
            turn='x'
    #label.skip
    print("skip~~~~~~~~~~")

def recognize():
    #nonlocal i
    #nonlocal turn
    if i > 4:
        if boarddic['1']==boarddic['2']==boarddic['3']!=' ':#==turn:
            print(turn, "win")
            exit()
            #break
            #goto.skip
        elif boarddic['4']==boarddic['5']==boarddic['6']!=' ':#==turn:
            print(turn, "win")
            exit()
            #break
            #goto.skip
        elif boarddic['7']==boarddic['8']==boarddic['9']!=' ':#=='turn':
            print(turn, "win")
            exit()
            #break
            #goto.skip
        elif boarddic['1']==boarddic['4']==boarddic['7']!=' ':#=='turn':
            print(turn, "win")
            exit()
            #break
            #goto.skip
        elif boarddic['2']==boarddic['5']==boarddic['8']!=' ':#=='turn':
            print(turn, "win")
            exit()
            #break
            #goto.skip
        elif boarddic['3']==boarddic['6']==boarddic['9']!=' ':#=='turn':
            print(turn, "win")
            exit()
            #break
            #goto.skip
        elif boarddic['3']==boarddic['5']==boarddic['7']!=' ':#=='turn':
            print(turn, "win")
            exit()
            #break
            #goto.skip
        elif boarddic['1']==boarddic['5']==boarddic['9']!=' ':#=='turn':
            print(turn, "win")
            exit()
            #break
            #goto.skip
#turn='x'
#i =0
if __name__ == "__main__":
    game()
