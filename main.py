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
    experience = 0
    resources_inventory = []
    items_inventory = []
    
class Item:
    gold = 1
    canSell = True
    
    def __init__(self,name,gold):
        self.name = name
        self.gold = gold
    
    def display(self):
        print("Item:", self.name)
        print("Sell value:", self.gold)
        
    def sell(self):
        if (self.canSell == True):
            return True
        else:
            return False
    
class Wood(Item): #Wood
    canSell = False
    gold = 2
    canSell = False
    def __init__(self):
        super().__init__("Wood", self.gold)
    
    def sell(self):
        return super().sell()
        
class Leather(Item): #Leather
    canSell = False
    gold = 3
    def __init__(self):
        super().__init__("Leather", self.gold)
    
    def sell(self):
        return super().sell()
        
class Iron(Item): #Iron
    canSell = False
    gold = 5 
    def __init__(self):
        super().__init__("Iron", self.gold)
        
    def sell(self):
        return super().sell()
    
class Gold(Item): #Gold
    canSell = False
    gold = 20
    def __init__(self):
        super().__init__("Gold", self.gold)
    
    def sell(self):
        return super().sell()
        
class Sword(Item): #Sword
    canSell = True
    gold = 400
    def __init__(self):
        super().__init__("Sword", self.gold)
        
    def sell(self):
        return super().sell()
    
    class Sword_Recipe(Item): #Sword recipe
        canSell = False
        gold = 150

        def display(self):
            print("Item:", self.name)
        
        def sell(self):
            return super().sell()

class Hammer(Item): #Hammer
    canSell = True
    gold = 200
    def __init__(self):
        super().__init__("Hammer", self.gold)
        
    def sell(self):
        return super().sell()

    class Hammer_Recipe(Item): #Hammer recipe
        canSell = False
        gold = 150

        def display(self):
            print("Item:", self.name)
        
        def sell(self):
            return super().sell()
        
class Bow(Item): #Bow
    canSell = True
    gold = 150
    def __init__(self):
        super().__init__("Bow", self.gold)
        
    def sell(self):
        return super().sell()
        
    class Bow_Recipe(Item): #Bow recipe
        canSell = False
        gold = 100

        def display(self):
            print("Item:", self.name)
        
        def sell(self):
            return super().sell()
        
class Helm(Item): #Helm
    canSell = True
    gold = 100
    def __init__(self):
        super().__init__("Helm", self.gold)
    
    def sell(self):
        return super().sell()
    
    class Helm_Recipe(Item): #Helm recipe
        canSell = False
        gold = 100

        def display(self):
            print("Item:", self.name)
        
        def sell(self):
            return super().sell()
        
class Chest(Item): #Chest
    canSell = True
    gold = 225
    def __init__(self):
        super().__init__("Chest", self.gold)
    
    def sell(self):
        return super().sell()
    
    class Chest_Recipe(Item): #Chest recipe
        canSell = False
        gold = 250

        def display(self):
            print("Item:", self.name)
        
        def sell(self):
            return super().sell()
        
class Feet(Item): #Feet
    canSell = True
    gold = 85
    def __init__(self):
        super().__init__("Feet", self.gold)
    
    def sell(self):
        return super().sell()

    class Feet_Recipe(Item): #Feet recipe
        canSell = False
        gold = 100

        def display(self):
            print("Item:", self.name)
        
        def sell(self):
            return super().sell()

#Principal game loop
def game_loop(day):
    #Setting classes into variables
    player = Player()
    myWood = Wood()
    myLeather = Leather()
    myIron = Iron()
    myGold = Gold()
    sword = Sword()
    hammer = Hammer()
    bow = Bow()
    helm = Helm()
    chest = Chest()
    feet = Feet()
    sword_recipe = Sword.Sword_Recipe("Sword recipe", Sword.Sword_Recipe.gold)
    hammer_recipe = Hammer.Hammer_Recipe("Hammer recipe", Hammer.Hammer_Recipe.gold)
    bow_recipe = Bow.Bow_Recipe("Bow recipe", Bow.Bow_Recipe.gold)
    helm_recipe = Helm.Helm_Recipe("Helm recipe", Helm.Helm_Recipe.gold)
    chest_recipe = Chest.Chest_Recipe("Chest recipe", Chest.Chest_Recipe.gold)
    feet_recipe = Feet.Feet_Recipe("Feet recipe", Feet.Feet_Recipe.gold)
    
    
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
                                "\n2. Buy recipes (You can only buy 1 recipe per day!)\n")
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
                    def buy_recipes():
                        os.system('clear') #Clear the previous console information and messages
                        print ("Gold: " + str(player.gold) + "\n")
                        command = input("1. Sword recipe " + str(sword_recipe.gold) +
                                        "\n2. Hammer recipe: " + str(hammer_recipe.gold) +
                                        "\n3. Bow recipe: " + str(bow_recipe.gold) +
                                        "\n4. Helm recipe: " + str(helm_recipe.gold) + 
                                        "\n5. Chest recipe: " + str(chest_recipe.gold) + 
                                        "\n6. Feet recipe: " + str(feet_recipe.gold) + "\n" +
                                        "\nWrite 'B' to get back and end you day!\n")
                        if command == "1": #Buy sword recipe
                            if player.gold >= sword_recipe.gold:
                                player.gold -= sword_recipe.gold
                                player.items_inventory.append(sword_recipe)
                            else:
                                print("\nYou do not have enough gold to buy this!")
                                print(input("\nPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "2": #Buy Hammer recipe
                            if player.gold >= hammer_recipe.gold:
                                player.gold -= hammer_recipe.gold
                                player.items_inventory.append(hammer_recipe)
                            else:
                                print("\nYou do not have enough gold to buy this!")
                                print(input("\nPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "3": #Buy Bow recipe
                            if player.gold >= bow_recipe.gold:
                                player.gold -= bow_recipe.gold
                                player.items_inventory.append(bow_recipe)
                            else:
                                print("\nYou do not have enough gold to buy this!")
                                print(input("\nPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "4": #Buy Helm recipe
                            if player.gold >= helm_recipe.gold:
                                player.gold -= helm_recipe.gold
                                player.items_inventory.append(helm_recipe)
                            else:
                                print("\nYou do not have enough gold to buy this!")
                                print(input("\nPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "5": #Chest recipe
                            if player.gold >= chest_recipe.gold:
                                player.gold -= chest_recipe.gold
                                player.items_inventory.append(chest_recipe)
                            else:
                                print("\nYou do not have enough gold to buy this!")
                                print(input("\nPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "6": #Buy Feet recipe
                            if player.gold >= feet_recipe.gold:
                                player.gold -= feet_recipe.gold
                                player.items_inventory.append(feet_recipe)
                            else:
                                print("\nYou do not have enough gold to buy this!")
                                print(input("\nPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "B":
                            pass
                        else:
                            print("\nChoose a right action!")
                            print(input("\nPress ENTER to continue!"))
                            buy_recipes() #Get back to the recipes buy menu
                        
                    buy_recipes() #Start the function
                    
                else:
                    print("\nChoose a right action!")
                    print(input("\nPress ENTER to continue"))
                    shop()
            
            shop()
            
        elif command == "2": #Let the player craft items
            def crafting(day):
                os.system('clear') #Clear the previous console information and messages
                if sword_recipe in player.items_inventory:
                        print("1. Sword (Need: 2 Woods and 3 Irons)")
                elif hammer_recipe in player.items_inventory:
                        print("2. Hammer")
                elif bow_recipe in player.items_inventory:
                        print("3. Bow")
                elif helm_recipe in player.items_inventory:
                        print("4. Helm")
                elif chest_recipe in player.items_inventory:
                        print("5. Chest")
                elif feet_recipe in player.items_inventory:
                        print("6. Feet")
                else:
                    print("You need a recipe to craft something!")
                    print(input("\nPress ENTER to continue"))
                    day -= 1
                    game_loop(day)
                    
                def sword_craft():
                    if int(sum(isinstance(x, Wood) for x in player.resources_inventory)) >= 2 and int(sum(isinstance(x, Iron) for x in player.resources_inventory)) >= 3: #If the player got the materials to craft then:
                        sword_materials = [myWood,myWood,myIron,myIron,myIron] #Materials needed to do the sword
                        for materials in sword_materials: #Remove the materials needed to do the sword
                            while materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(sword_recipe)    
                        
                        player.items_inventory.append(sword)
                    else:
                        print("\nYou don't have all the materials to craft this!")
                        print(input("\nPress ENTER to continue"))
                        
                command = input()
                if (command == "1") and (sword_recipe in player.items_inventory):
                    sword_craft()
                else:
                    print("Choose a right action!")

            crafting(day)
                        
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