import time as t
import random as r
char = "#"
def clear_screen():
    print("\n"*52)  #Clears the screen of the last print to give the illusion of "frames"


def position_bullet(x):
    display_empty = '                    '
    display_1 = char + '-                   ' + "#"
    display_2 = char + ' -                  ' + "#"
    display_3 = char + '  -                 ' + "#"
    display_4 = char + '   -                ' + "#"
    display_5 = char + '    -               ' + "#"
    display_6 = char + '     -              ' + "#"
    display_7 = char + '      -             ' + "#"
    display_8 = char + '       -            ' + "#"
    display_9 = char + '        -           ' + "#"
    display10 = char + '         -          ' + "#"
    display11 = char + '          -         ' + "#"
    display12 = char + '           -        ' + "#"
    display13 = char + '            -       ' + "#"
    display14 = char + '             -      ' + "#"
    display15 = char + '              -     ' + "#"
    display16 = char + '               -    ' + "#"
    display17 = char + '                -   ' + "#"
    display18 = char + '                 -  ' + "#"
    display19 = char + '                  - ' + "#"
    display20 = char + '                   -' + "#"
    if x == "no":
        print(display_empty)
    if x == 1:
        print(display_1)
    if x == 2:
        print(display_2)
    if x == 3:
        print(display_3)
    if x == 4:
        print(display_4)
    if x == 5:
        print(display_5)
    if x == 6:
        print(display_6)
    if x == 7:
        print(display_7)
    if x == 8:
        print(display_8)
    if x == 9:
        print(display_9)
    if x == 10:
        print(display10)
    if x == 11:
        print(display11)
    if x == 12:
        print(display12)
    if x == 13:
        print(display13)
    if x == 14:
        print(display14)
    if x == 15:
        print(display15)
    if x == 16:
        print(display16)
    if x == 17:
        print(display17)
    if x == 18:
        print(display18)
    if x == 19:
        print(display19)
    if x == 20:
        print(display20)


def user_fire():
    x = 1
    for n in range(20):
        position_bullet(x)
        x = x + 1
        t.sleep(0.07)
        clear_screen()


def enemy_fire():
    x = 20
    for n in range(20):
        position_bullet(x)
        x = x - 1
        t.sleep(0.07)
        clear_screen()





hp = 100  #Sets user health points
hp2 = 100  #Sets enemy health points
coins = 0 #Sets coins to 0
shield = "🛡" #Defines how the shield looks.
shield_price = 50
health_potion = "🧪"
health_potion_price = 125
evade_chance = r.randint(1, 4)
difficulty_choice = input("Would you like difficulty 1 or 2? ")
while int(difficulty_choice) != 1 and int(difficulty_choice)!= 2:
  print("Invalid input.")
  difficulty_choice = input("WOuld you like difficulty 1 or 2? ")
if int(difficulty_choice) == 2:
  hp2 = 300
  coins = 50
  print("You have selected hard difficulty. You will start with 50 coins, and your opponent will have 300 health points.")
else:
  print("You have selected the normal difficulty.")


print("Welcome to Dominic's game! ")
t.sleep(1)
print("In this game, you are a hashtag, and your opponenent is a hashtag. ")
t.sleep(1)
print("Your goal is to reduce your opponents health to 0.")
t.sleep(1)
print("The amount of coins ⏣ you get depends on how much damage you do.")
t.sleep(1)
print("You can buy items from the shop, based off of how many coins you have.")
t.sleep(1)
print("The rest is self-explanatory.")
t.sleep(2)
while True:
    print("You have ⏣ " + str(coins) + ", your opponent has " + str(hp2) + "health, and you have " + str(hp) + " health.")
    choice = input("Type Y to attack, or type S to go to the shop. ") 
    if coins < 50 and choice.upper == "S":
        print("Either you are too poor to go to the shop, or you typed something that was not an option.")
        while choice.upper() != "Y":
          print("Invalid input")
          choice = input("Type Y to attack, or type S to go to the shop. ")
    while choice.upper() != "Y" and choice.upper() != "S":
      print("That is an invalid input, please try again.")
      print("You have ⏣ " + str(coins) + ", your opponent has " + str(hp2) + " health, and you have " + str(hp) + " health.")
      choice = input("Type Y to attack, or type S to go to the shop.")
    if choice.upper() == "Y":
        user_fire()
        damage = r.randint(20, 40)
        if hp2 <= 150 and evade_chance == 4 and int(difficulty_choice) == 2:
          print("Oh no! The enemy evaded your attack!")
          t.sleep(2)
          damage = 0
        evade_chance = r.randint(1, 4)
        hp2 = hp2 - damage
        coins = coins + damage
        print("You have ⏣ " + str(coins) + "!")
        if hp <= 0 or hp2 <= 0:
          break
        print("The enemy has " + str(hp2) + " health.")
        t.sleep(2)
    elif choice.upper() == "S":
      print("You can buy a shield for 50 coins.")
      print("You can also buy a health potion for 125 coins.")
      buy = input("Type H to buy health potion, and type S to buy a shield.")
      while buy.upper() != "S" and buy.upper() != "H":
        print("Invalid input.")
        buy = input("Type H to buy health potion, and type S to buy a shield.")
      if buy.upper() == "S":
        if coins >= shield_price:
          coins = coins - shield_price
          char = char + "🛡"
      elif buy.upper() == "H":
        if coins >= health_potion_price:
          coins = coins - health_potion_price
          print(char + health_potion)
          hp = hp + 100
          t.sleep(2)
          clear_screen()
          print("You drank a health potion!" + "\n"*3)
          print(char)
          t.sleep(3)
        else:
          print("You do not have enough coins")
    enemy_fire()
    if char == "#🛡":
      hp = hp - r.randint(10, 20)
    else:
      hp = hp - r.randint(20, 40)
    if hp <= 0 or hp2 <= 0:
      break
    print("You have " + str(hp) + " health.")
    t.sleep(2)

if hp > 0:
  print("Awesome job! You won!")
else:
  print("You lost...")
