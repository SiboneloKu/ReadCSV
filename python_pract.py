from random import randint


boad=[]

for x in range(0, 5):
    boad.append(["0"]*5)

def print_board(boad):
    for row in boad:
        print(" ".join(row))
    return ""

#print (print_board(boad))

def random_row(boad):
    return randint(0,len(boad)-1)

def random_col(boad):
    return randint(0,len(boad)-1)



ship_row = random_row(boad)
ship_col = random_col(boad)
print (ship_row)
print(ship_col)

print ("Hi! Welcome to the number guessing game.\nYou have to guess a row number "
       "from 0-4 and a column number from 0-4.\n"
       "If you guess right you will find a star which is hidden on "
       "row and column number\nbut if you guessed wrong you will see an X")
print("You have 4 chances.\nLET THE GAME BEGING")

for times in range(4):
    print ("chance number",times+1)

    vara=0
    vara2=0
    while True:
        try:
            vara=int(input("Guess a Row"))
            vara2=int(input("Guess a Col"))
        except ValueError:
              print("Enter numbers only")
              continue
        else:
            break


    guess_row=vara
    guess_col=vara2


    if guess_row==ship_row and guess_col==ship_col:
      print("Yayi!!!!!! you won the guessing game")
      boad[guess_row][guess_col]="*"
      print(print_board(boad))
      break
    else:
      if guess_row not in range(5) or \
            guess_col not in range(5):
        print("The numbers you entered are not a range please,\n please make sure the number are between 0-4")

      elif boad[guess_row][guess_col]=="X":
        print("you have already guessed these number")
      else:
        print("Eish :( :( :( you missed")
        boad[guess_row][guess_col]="X"

      if times == 3:
        print("Game Over")

      print (print_board(boad))











