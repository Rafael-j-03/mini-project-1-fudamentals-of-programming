import os #Let he work with operating system functions
from collections import deque

os.system('clear') #Clear the previous console information and messages

#Game explanation
print("In this game you have to get a profit of 100k in gold to win, or you lose all your money and lose.")
print(input("\nPress ENTER to continue"))
os.system('clear') #Clear the previous console information and messages

#variables
day = 0

#Inventory and items
class Player:
    gold = 250
    resources_inventory = []
    items_inventory = []
    
class Item:
    gold = 1
    
    def __init__(self,name,gold):
        self.name = name
        self.gold = gold
        
    def item_gold(self,gold):
        self.gold = gold
    
    def display(self):
        print("Item:", self.name)
        print("Sell value;", self.gold)
    
class Wood(Item):
    gold = 2
    def __init__(self):
        super().__init__("Wood", self.gold)
        
class Leather(Item):
    gold = 3
    def __init__(self):
        super().__init__("Leather", self.gold)
        
class Iron(Item):
    gold = 5 
    def __init__(self):
        super().__init__("Iron", self.gold)
        
class Gold(Item):
    gold = 20
    def __init__(self):
        super().__init__("Gold", self.gold)
        
class Sword(Item):
    gold = 400
    def __init__(self):
        super().__init__("Sword", self.gold)
        
class Hammer(Item):
    gold = 200
    def __init__(self):
        super().__init__("Hammer", self.gold)
        
class Bow(Item):
    gold = 150
    def __init__(self):
        super().__init__("Bow", self.gold)
        
class Helm(Item):
    gold = 100
    def __init__(self):
        super().__init__("Helm", self.gold)
        
class Chest(Item):
    gold = 225
    def __init__(self):
        super().__init__("Chest", self.gold)
        
class Feet(Item):
    gold = 85
    def __init__(self):
        super().__init__("Feet", self.gold)

#Principal game loop
def game_loop(day):
    #Setting classes into variables
    myWood = Wood()
    myLeather = Leather()
    myIron = Iron()
    myGold = Gold()
    player = Player()
    
    #The game will continue until the player has no gold or gets 100k
    while (player.gold >= 0) and (player.gold <= 100000):
        os.system('clear') #Clear the previous console information and messages
        day = day + 1
        print("Day:",day,"\n")
        command = input("What do you wanna do in this day?\n" +
                        "1. Buy Items\n"+
                        "2. Craft Items\n"+
                        "3. Sell items\n" +
                        "4. See your inventory (This action will not occupy your day)\n")
        if command == "1": #Let the player buy things
            def shop():
                os.system('clear') #Clear the previous console information and messages
                print ("Gold: " + str(player.gold) + "\n")
                command = input("What do you wanna do?"+
                                "\n1. Buy resources" +
                                "\n2. Buy recipes\n")
                if command == "1": #Let the player buy resources
                    def buy_resources():
                        os.system('clear') #Clear the previous console information and messages
                        print ("Gold: " + str(player.gold) + "\n")
                        command = input("1. Wood: " + str(myWood.gold) +
                                            "\n2. Leather: " + str(myLeather.gold) +
                                            "\n3. Iron: " + str(myIron.gold) +
                                            "\n4. Gold: " + str(myGold.gold) + "\n" + 
                                            "\nWrite 'B' to get back and end you day!\n")
                        if command == "1": #Buy wood
                            if player.gold >= myWood.gold:
                                player.gold -= myWood.gold
                                player.resources_inventory.append(myWood)
                                buy_resources() #Get back to the function if the player wants to buy more resources
                            else:
                                print("\nYou do not have enough gold to buy this!")
                                print(input("\nPress ENTER to continue!"))
                                buy_resources() #Get back to the function if the player wants to buy more resources
                        elif command == "2": #Buy leather
                            if player.gold >= myLeather.gold:
                                player.gold -= myLeather.gold
                                player.resources_inventory.append(myLeather)
                                buy_resources() #Get back to the function if the player wants to buy more resources
                            else:
                                print("\nYou do not have enough gold to buy this!")
                                print(input("\nPress ENTER to continue!"))
                                buy_resources() #Get back to the function if the player wants to buy more resources
                        elif command == "3": #Buy iron
                            if player.gold >= myIron.gold:
                                player.gold -= myIron.gold
                                player.resources_inventory.append(myIron)
                                buy_resources() #Get back to the function if the player wants to buy more resources
                            else:
                                print("\nYou do not have enough gold to buy this!")
                                print(input("\nPress ENTER to continue!"))
                                buy_resources() #Get back to the function if the player wants to buy more resources
                        elif command == "4": #Buy gold
                            if player.gold >= myGold.gold:
                                player.gold -= myGold.gold
                                player.resources_inventory.append(myGold)
                                buy_resources() #Get back to the function if the player wants to buy more resources
                            else:
                                print("\nYou do not have enough gold to buy this!")
                                print(input("\nPress ENTER to continue!"))
                                buy_resources() #Get back to the function if the player wants to buy more resources
                        elif command == "B":
                            pass
                        else:
                            print("\nChoose a right action!")
                            print(input("\nPress ENTER to continue!"))
                            buy_resources()
   
                    buy_resources() #Executes the function
                
                elif command == "2": #Let the player buy recipes
                    pass
                else:
                    print("\nChoose a right action!")
                    print(input("\nPress ENTER to continue"))
                    shop()
            
            shop()
            
        elif command == "2": #Let the player craft items
            pass
        elif command == "3": #Let the player sell his items
            pass
        elif command == "4": #Show to the player his inventory
            os.system('clear') #Clear the previous console information and messages
            day -= 1
            print("Gold:",player.gold)
            print("-------")
            print("Resources:\n"+
                  "Wood: " + str(sum(isinstance(x, Wood) for x in player.resources_inventory)) + " /"+ 
                  " Leather: " + str(sum(isinstance(x, Leather) for x in player.resources_inventory)) + " /" +
                  " Iron: " + str(sum(isinstance(x, Iron) for x in player.resources_inventory)) + " /" +
                  " Gold: " + str(sum(isinstance(x, Gold) for x in player.resources_inventory)))
            print("-------")
            for item in Player.items_inventory:
                item.display()
                print("-------")
            print(input("\n\nPress ENTER to get back to the main menu"))
            if command == "":
                pass
        else:
            day -= 1
            print("\nChoose a right action!")
            print(input("\nPress ENTER to continue"))
            game_loop(day)

game_loop(day)