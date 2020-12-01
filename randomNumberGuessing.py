#WAP in python to generate random number only three time if the guess numbr is equal to
# random number generatd then increase the counter by 1 and if not then decrease the counter by 1 if the
# total value reached maximum to 25 then Player win the matched if not then failed or loose the game.

#Solution

import random
#making three turns and global variables of sum declaration
turn = 3
sum = 0

while turn >= 1:
    inp= int(input("Enter the guess number less than 25:.."))
    if inp <= 25:

      number = random.randint(0,25)
      if number == inp:
        turn = turn+1
        print("Congratulations, one more chance added.")
        print()
      else:
        turn = turn-1
        print("Sorry, not matched.")
        print()
    else:
        print("invalid input, greater than 25.")
    sum = sum+inp
print()
if(sum == 25):
    print("Congratulations, You have make your sum ", sum, "and you have won the Game")
else:
    print("Sorry, You have loose the game.")



'''Enter the guess number less than 25:..14
Sorry, not matched.

Enter the guess number less than 25:..15
Sorry, not matched.

Enter the guess number less than 25:..16
Sorry, not matched.


Sorry, You have loose the game.'''
