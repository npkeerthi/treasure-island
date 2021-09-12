print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
A=input("after walking for awhile you got two ways which one would you choose: left/right \n:")
a=A.lower()
if(a=="left"):
  print("now u got a island would you swim or wait or sleep:")
  b=(input()).lower()
  if(b=="swim"):
    print("OH NO sharks!!...GAME OVER")
  elif(b=="sleep"):
    print("Holyshit snake on you?..GAME OVER")
  elif(b=="wait"):
    print("after waiting for a while you got into a ship which took you to a RESORT\n you saw a diamond beside the fountain door would you pickup(1) or get into door(2) \n 1 or 2 :")
    c=input()
    if(c=="1"):
      print("SECURITY BUSTED YOU GAME OVER")
    elif(c=="2"):
      print("YEEAH!! YOU FOUND THE TREASURE!!")
elif(a=="right"):
  b=(input("OMG You gotta climb mountain(1) or walk through a whole(2) else theres a black water lake jump into it(3) ? \n:")).lower()
  if(b=="1"):
    print("YOU FELL DOWN... Game Over..")
  elif(b=="2"):
    print("OOH why so curious 😂 now the whole got closed by some stones U R STUCK ..🔚")
  else:
    print("It wasn't a pool you got sunk ..WASTED!!")



#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload