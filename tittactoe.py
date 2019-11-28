'''
Created on Nov 25, 2019

@author: Rishaba Priyan
'''
#dictionary that stores the position and values
ttt = {'1':' ','2':' ','3':' ',
    '4':' ','5':' ','6':' ',
    '7':' ','8':' ','9':' '};
#returns True if all three variables are same
def combination(a,b,c):
    
    if(ttt[a] == ttt[b] and ttt[b] == ttt[c] and ttt[c]== ttt[a] and ttt[a]!=' '):
        return True
    else:
        return False
#returns True if there is a win probability
def win_check():
    if(combination('1','5','9') | combination('2','5','8') | combination('3','5','7') | combination('6','5','4') | combination('1','2','3') | combination('4','5','6') | combination('7','8','9') | combination('1','4','7') | combination('3','6','9') ):
        return True  
#Function to print the game   
def play (choice,player):
    ttt[choice]=player
    print(ttt['1']+'|'+ttt['2']+'|'+ttt['3'])
    print('__'+'__'+'__')
    print(ttt['4']+'|'+ttt['5']+'|'+ttt['6'])
    print('__'+'__'+'__')
    print(ttt['7']+'|'+ttt['8']+'|'+ttt['9'])
#
print('Choice Pattern reference for tic tac toe')
#intial reference layout
print('1|2|3')
print('__'+'__'+'__')
print('4|5|6')
print('__'+'__'+'__')
print('7|8|9')

#program begins here
player='X'
for turn in range(9):
    print('Player '+player+'\'s turn')
    print('Enter your position:')
    choice=input()
    play(choice,player)
    win_chk=win_check()
    if(win_chk):
        print('Player \''+player+'\' won')
        break
    if (player == 'X'):#---------------------alternates platers turn
        player='O'
    else:
        player='X'
        
