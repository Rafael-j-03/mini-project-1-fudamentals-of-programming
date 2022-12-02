import os #Let he work with operating system functions

os.system('clear') #Clear the previous console information and messages

#Game explanation
print("In this game you have to get a profit of 100k in gold to win, or you lose all your money and lose.")
print(input("\nPress ENTER to continue"))
os.system('clear') #Clear the previous console information and messages

#variables
day = 0
gold = 250

#Inventory and items
class Item:
    pass
class Resource(Item):
    pass
class Wood(Resource):
    pass
class Iron(Resource):
    pass
class Leather(Resource):
    pass
class Gold(Resource):
    pass
class Sword(Item):
    pass
class Hammer(Item):
    pass
class Armor(Item):
    pass
class Bow(Item):
    pass
class Helm(Armor):
    pass
class Chest(Armor):
    pass
class Feet(Armor):
    pass

#Principal game loop
while (gold >= 0) and (gold <= 100000):
    day = day + 1
    print("Day:",day,"\n")
    command = input("What do you wanna do in this day?\n" +
                    "1. Buy resources\n"+
                    "2. Craft Items\n"+
                    "3. Sell items\n")
    if command == "1":
        pass
    elif command == "2":
        pass
    elif command == "3":
        pass
    os.system('clear') #Clear the previous console information and messages