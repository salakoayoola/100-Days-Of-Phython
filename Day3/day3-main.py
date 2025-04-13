#Print an ASCII art of the trasure maze
print('''
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/

''')
print("Welcome to the Amazon Rainforest Treasure Maze!")
print("Your mission is to find the treasure.")
direction1 = input('You are at the first crossroad. Where do you want to go? Type "left" or "right"').lower()
if direction1 == "left":
    # print('''
    #             /||
    #         /_|_|
    #         /__|_|
    #         ____|____
    #         \_o_o_o_/
    #         ~~ |     ~~~~~
    #         ___t_________ 
    #       ''')
    direction2 = input('You have reached a lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if direction2 == "wait":
        print('''
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|
''')
        direction3 = input('The boat takes you to the other side, choose a door. Type "Red", "Green", or "Yellow".').lower()
        if direction3 == "red":
            print("You enter a Python's Den! Game Over.")
        elif direction3 == "green":
            print("Green, the home of the poisonous dart frog! Game Over.")
        elif direction3 == "yellow":
            print("Congratulations! You found the treasure!")
        else:
            print("You chose a door that doesn't exist. The Chimpanzee gang took you. Game Over!")
    elif direction2 == "swim":
        print('''        ,---,
  _    _,-'    `--,
 ( `-,'            `-
  \           ,    o `
  /   ,       ;       `-
 (_,-' \       `, _  ""/
        `-,___ =='__,-'
              ```` ''')
        print("You chose to swim in an infamous Piranha lake! Game Over.")
else:
    print("Game Over! You walked into Quicksand.")
    print('''      ________________________________         
      /                                "-_          
     /      .  |  .                       \          
    /      : \ | / :                       \         
   /        '-___-'                         \      
  /_________________________________________ \      
       _______| |________________________--""-L 
      /       F J                              \ 
     /       F   J                              L
    /      :'     ':                            F
   /        '-___-'                            / 
  /_________________________________________--"  ''')