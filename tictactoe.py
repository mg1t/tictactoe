#tictactoe von mg1t 11.02.2021
import os

slot=[-1,-1,-1,-1,-1,-1,-1,-1,-1]
winner=-1;
player=1;

def print_slot(input):
    if (input==1): print(" X ", end="")
    elif(input==2): print(" O ", end="")
    else:   print("   " ,end="")

def print_board(input):
    os.system("cls")
    position=0
    print(" --- --- ---      --- --- ---")
    print("|",end="")
    while (position < 9):
        print_slot(input[position])
        if(position == 2):
            print("|    | 7 | 8 | 9 |")
            print(" --- --- ---      --- --- ---")
            print("|",end="")
        elif(position==5):
            print("|    | 4 | 5 | 6 |")
            print(" --- --- ---      --- --- ---")
            print("|",end="")
        elif (position==8):
            print("|    | 1 | 2 | 3 |")
            print(" --- --- ---      --- --- ---")
        else:
            print("|",end="")
        position=position+1
    
def check_winner(input):
    if(input[0]==input[1]) and (input[1]==input[2]) and (input[0] != -1): winner=input[0];
    elif(input[3]==input[4]) and (input[4]==input[5]) and (input[3] != -1): winner=input[3];
    elif(input[6]==input[7]) and (input[7]==input[8]) and (input[3] != -1): winner=input[8];
    elif(input[0]==input[3]) and (input[3]==input[6]) and (input[0] != -1): winner=input[0];
    elif(input[1]==input[4]) and (input[4]==input[7]) and (input[1] != -1): winner=input[1];
    elif(input[2]==input[5]) and (input[5]==input[8]) and (input[2] != -1): winner=input[2];
    elif(input[0]==input[4]) and (input[4]==input[8]) and (input[0] != -1): winner=input[0];
    elif(input[2]==input[4]) and (input[4]==input[6]) and (input[2] != -1): winner=input[2];
    else: winner=-1;
    
    if((-1) in input)==False: winner=0;
    
    return winner;
    
    
print_board(slot);
    
while(winner==-1):
    allowed=False;
    while(allowed==False):
        print("\nSpieler ",player," Bitte Position wählen: ",end="");
        pos=-1;
        new_pos=int(input());
        #Tasten tauschen:
        if new_pos==1: pos=6;
        elif new_pos==2: pos=7;
        elif new_pos==3: pos=8;
        elif new_pos==4: pos=3;
        elif new_pos==5: pos=4;
        elif new_pos==6: pos=5;
        elif new_pos==7: pos=0;
        elif new_pos==8: pos=1;
        elif new_pos==9: pos=2;
        else:pos=-1;
        if pos!=-1: 
            if (slot[pos]==-1):allowed=True;
            else: print("Bereits belegt, bitte neu wählen!");
    slot[pos]=player;
    print_board(slot);
    winner=check_winner(slot);
    if (player==1): player=2;
    else: player=1;
    
if winner==0: print("\nKein Gewinner :(\n");
else: print("\nGewinner: Spieler",winner,"\n");
        
