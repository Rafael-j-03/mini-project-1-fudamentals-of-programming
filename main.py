import os #Let he work with operating system functions
import random #Random library - can set random numbers

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
    experience = 1
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
        print("Average selling price:", self.gold)
        
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
    gold = 800
    successCrafting = 5
    
    def __init__(self):
        super().__init__("Sword", self.gold)
        
    def sell(self):
        return super().sell()
    
    class Sword_Recipe(Item): #Sword recipe
        canSell = False
        gold = 200

        def display(self):
            print("Item:", self.name)
        
        def sell(self):
            return super().sell()

class Hammer(Item): #Hammer
    canSell = True
    successCrafting = 4
    gold = 600
    
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
    successCrafting = 3
    gold = 400
    
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
    gold = 400
    successCrafting = 3
    
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
    gold = 1000
    successCrafting = 6
    
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
    gold = 300
    successCrafting = 3
    
    def __init__(self):
        super().__init__("Feet", self.gold)
    
    def sell(self):
        return super().sell()

    class Feet_Recipe(Item): #Feet recipe
        canSell = False
        gold = 75

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
    recipes = [sword_recipe,hammer_recipe,bow_recipe,helm_recipe,chest_recipe,feet_recipe]
    
    player.items_inventory.append(sword)
    player.items_inventory.append(sword)
    player.items_inventory.append(sword)
    player.items_inventory.append(sword)
    
    #The game will continue until the player has no gold or gets 100k
    while (player.gold > 0) and (player.gold <= 100000):
        #Variables that need to be updated
        woodInInventory = sum(isinstance(x, Wood) for x in player.resources_inventory)
        leatherInInventory = sum(isinstance(x, Leather) for x in player.resources_inventory)
        ironInInventory = sum(isinstance(x, Iron) for x in player.resources_inventory)
        goldInInventory = sum(isinstance(x, Gold) for x in player.resources_inventory)
        day += 1
        #Player Craft Attempt
        d10 = random.randint(1,10) #Ten-sided dice
        playerCraftAttempt = player.experience * d10
        
        os.system('clear') #Clear the previous console information and messages
        
        print("Day:",day,"\n") #Print the current day
        
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
                                            "\nOr write 'B' to get back and end you day!\n")
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
                                        "\nOr write 'B' to get back and end you day!\n")
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
            def crafting():
                os.system('clear') #Clear the previous console information and messages
                if sword_recipe in player.items_inventory:
                        print("1. Sword (Needed: 2 Woods and 3 Irons)")
                if hammer_recipe in player.items_inventory:
                        print("2. Hammer (Needed: 2 Woods and 4 Irons)")
                if bow_recipe in player.items_inventory:
                        print("3. Bow (Needed: 5 Woods, 1 Iron and 2 Leathers)")
                if helm_recipe in player.items_inventory:
                        print("4. Helm (Needed: 3 Irons and 1 Gold)")
                if chest_recipe in player.items_inventory:
                        print("5. Chest (Needed: 5 Irons and 2 Golds)")
                if feet_recipe in player.items_inventory:
                        print("6. Feet (Needed: 2 Irons and 2 Golds)")
                        
                #Check if any recipe is in the player's inventory
                checkRecipes = any(n in recipes for n in player.items_inventory)
                if checkRecipes is False:
                    print("You need a recipe to craft something!")
                    print(input("\nPress ENTER to continue"))
                    pass
                    
                def sword_craft(): #Craft sword
                    if int(woodInInventory) >= 2 and int(ironInInventory) >= 3: #If the player got the materials to craft then:
                        sword_materials = [myWood,myWood,myIron,myIron,myIron] #Materials needed to do the sword
                        for materials in sword_materials: #Remove the materials needed to do the sword
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(sword_recipe)
                        if playerCraftAttempt >= sword.successCrafting: #Success craft attempt
                            player.items_inventory.append(sword)
                            player.experience += 1
                            print("\nYou have crafted a sword!")
                            print(input("\nPress ENTER to continue"))
                        if playerCraftAttempt < sword.successCrafting: #Failed craft attempt
                            print("\nYou have failed to craft a sword!")
                            print(input("\nPress ENTER to continue"))
                    else:
                        print("\nYou don't have all the materials to craft this!")
                        print(input("\nPress ENTER to continue"))
                            
                def hammer_craft(): #Craft hammer
                    if int(woodInInventory) >= 2 and int(ironInInventory) >= 4: #If the player got the materials to craft then:
                        hammer_materials = [myWood,myWood,myIron,myIron,myIron,myIron] #Materials needed to do the hammer
                        for materials in hammer_materials: #Remove the materials needed to do the hammer
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(hammer_recipe)
                        if playerCraftAttempt >= hammer.successCrafting: #Success craft attempt
                            player.items_inventory.append(hammer)
                            player.experience += 1
                            print("\nYou have crafted a hammer!")
                            print(input("\nPress ENTER to continue"))  
                        if playerCraftAttempt < hammer.successCrafting: #Failed craft attempt
                            print("\nYou have failed to craft a hammer!")
                            print(input("\nPress ENTER to continue"))
                    else:
                        print("\nYou don't have all the materials to craft this!")
                        print(input("\nPress ENTER to continue"))

                def bow_craft(): #Craft bow
                    if int(woodInInventory) >= 5 and int(ironInInventory) >= 1 and int(leatherInInventory) >= 2: #If the player got the materials to craft then:
                        bow_materials = [myWood,myWood,myWood,myWood,myWood,ironInInventory,leatherInInventory, leatherInInventory] #Materials needed to do the bow
                        for materials in bow_materials: #Remove the materials needed to do the bow
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(bow_recipe)
                        if playerCraftAttempt >= bow.successCrafting: #Success craft attempt
                            player.items_inventory.append(bow)
                            player.experience += 1
                            print("\nYou have crafted a bow!")
                            print(input("\nPress ENTER to continue"))
                        if playerCraftAttempt < bow.successCrafting: #Failed craft attempt
                            print("\nYou have failed to craft a bow!")
                            print(input("\nPress ENTER to continue"))
                    else:
                        print("\nYou don't have all the materials to craft this!")
                        print(input("\nPress ENTER to continue"))
                        
                def helm_craft(): #Craft helm
                    if int(ironInInventory) >= 3 and int(goldInInventory) >= 1: #If the player got the materials to craft then:
                        helm_materials = [myIron,myIron,myIron,myGold] #Materials needed to do the helm
                        for materials in helm_materials: #Remove the materials needed to do the helm
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(helm_recipe)
                        if playerCraftAttempt >= helm.successCrafting: #Success craft attempt
                            player.items_inventory.append(helm)
                            player.experience += 1
                            print("\nYou have crafted a helm!")
                            print(input("\nPress ENTER to continue"))  
                        if playerCraftAttempt < helm.successCrafting: #Failed craft attempt
                            print("\nYou have failed to craft a helm!")
                            print(input("\nPress ENTER to continue"))
                    else:
                        print("\nYou don't have all the materials to craft this!")
                        print(input("\nPress ENTER to continue"))

                def chest_craft(): #Craft chest
                    if int(ironInInventory) >= 5 and int(goldInInventory) >= 2: #If the player got the materials to craft then:
                        chest_materials = [myIron,myIron,myIron,myIron,myIron,myGold,myGold] #Materials needed to do the chest
                        for materials in chest_materials: #Remove the materials needed to do the chest
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(chest_recipe)
                        if playerCraftAttempt >= chest.successCrafting: #Success craft attempt
                            player.items_inventory.append(chest)
                            player.experience += 1
                            print("\nYou have crafted a chest!")
                            print(input("\nPress ENTER to continue"))  
                        if playerCraftAttempt < chest.successCrafting: #Failed craft attempt
                            print("\nYou have failed to craft a chest!")
                            print(input("\nPress ENTER to continue"))
                    else:
                        print("\nYou don't have all the materials to craft this!")
                        print(input("\nPress ENTER to continue"))
                        
                def feet_craft(): #Craft feet
                    if int(ironInInventory) >= 2 and int(goldInInventory) >= 2: #If the player got the materials to craft then:
                        feet_materials = [myIron,myIron,myGold,myGold] #Materials needed to do the feet
                        for materials in feet_materials: #Remove the materials needed to do the feet
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(feet_recipe)
                        if playerCraftAttempt >= feet.successCrafting: #Success craft attempt
                            player.items_inventory.append(feet)
                            player.experience += 1
                            print("\nYou have crafted a feet!")
                            print(input("\nPress ENTER to continue"))  
                        if playerCraftAttempt < feet.successCrafting: #Failed craft attempt
                            print("\nYou have failed to craft a feet!")
                            print(input("\nPress ENTER to continue"))
                    else:
                        print("\nYou don't have all the materials to craft this!")
                        print(input("\nPress ENTER to continue"))
                
                def choose_craft(): #Let the player select what we wants to craft
                    print("\nOr write 'B' to get back home. (You will lose your day)")
                    command = input()
                    if (command == "1") and (sword_recipe in player.items_inventory):
                            sword_craft()
                    elif (command == "2") and (hammer_recipe in player.items_inventory):
                            hammer_craft()
                    elif (command == "3") and (bow_recipe in player.items_inventory):
                            bow_craft()
                    elif (command == "4") and (helm_recipe in player.items_inventory):
                            helm_craft()
                    elif (command == "5") and (chest_recipe in player.items_inventory):
                            chest_craft()
                    elif (command == "6") and (feet_recipe in player.items_inventory):
                            feet_craft()
                    elif command == "B":
                        pass
                    else:
                        print("Choose a right action!")
                        print(input("\nPress ENTER to continue"))
                        crafting()
                
                if checkRecipes is True:
                    choose_craft()
                    
            crafting()
                        
        elif command == "3": #Let the player sell his items
            os.system('clear') #Clear the previous console information and messages
            clients = 3 #Random number of clients per day
            sellable_items = [sword,hammer,bow,helm,chest,feet]
            items = []
    
            def offer(): #Client offer
                items = []
                for i in sellable_items:
                    if i in player.items_inventory:
                        items.append(i)
                if any(items):
                    client_choice = random.choice(items) #Item that the client is going to choose
                    client_offer = client_choice.gold * random.uniform(0.5,1.5) #Initial client's offer
                    if client_choice in player.items_inventory: #Check if the item is in the player's inventory
                        def proposal_decision():
                            os.system('clear') #Clear the previous console information and messages
                            print("Client: I offer you this - " + str(round(client_offer))  + " Gold - " + "for: " + client_choice.name)
                            command = input("\nDo you want to accept it? (Y/N)\n")
                            if command == "Y":
                                player.gold += round(client_offer)
                                print("\nCurrent Gold:",player.gold)
                                player.items_inventory.remove(client_choice)
                                print(input("\nPress ENTER to continue"))
                            elif command == "N":
                                pass
                            else:
                                print("\nChoose a right action!")
                                print(input("\nPress ENTER to continue"))
                                proposal_decision()
                    else:
                        pass
                            
                    proposal_decision()
                
            
                return items
                    
            def selling_items(items): #Selling items
                if clients > 0: #If there's client on the shop:
                    for i in range(clients):
                        offer()
                    else: #If the player got nothing to sell
                        os.system('clear') #Clear the previous console information and messages
                        print("You have got nothing left to sell!")
                        print(input("\nPress ENTER to get back to the main menu"))
                
                if clients == 0: #If there's no clients on the shop:
                    print("You have no clients today.")
                    print(input("\nPress ENTER to get back to the main menu"))
            
            selling_items(items) #Execute the function to sell items
        
        elif command == "4": #Show to the player his inventory
            os.system('clear') #Clear the previous console information and messages
            day -= 1
            print("Gold:",player.gold)
            print("-------")
            print("Player level:",player.experience)
            print("-------")
            print("Resources:\n"+
                  "Wood: " + str(woodInInventory) + " /" + 
                  " Leather: " + str(leatherInInventory) + " /" +
                  " Iron: " + str(ironInInventory) + " /" +
                  " Gold: " + str(goldInInventory))
            print("-------")
            for item in player.items_inventory:
                item.display()
                print("-------")
            print(input("\n\nPress ENTER to get back to the main menu"))
            if command == "":
                pass
        else:
            day -= 1
            print("\nChoose a right action!")
            print(input("\nPress ENTER to continue"))
            pass

game_loop(day)