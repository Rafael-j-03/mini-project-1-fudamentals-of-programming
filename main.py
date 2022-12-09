import os #Let he work with operating system functions
import random #Random library - can set random numbers

os.system('clear') #Clear the previous console information and messages

#Game explanation
print("\033[1;37mIn this game you have to get a profit of 50k in gold to win, or you lose all your money and lose.")
print(input("\n\033[1;33mPress ENTER to continue"))
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
    def __init__(self,name,gold):
        self.name = name
        self.gold = gold
    
    def display(self):
        print("\033[0;36mItem:\033[1;37m", self.name)
        print("\033[0;36mAverage selling price:", self.gold)
        
class Recipes:
    def __init__(self,name,gold):
        self.name = name
        self.gold = gold
    
    def display(self):
        print("\033[0;36mItem:Item:\033[1;37m", self.name)
    

class Wood(Item): #Wood
    gold = 2
    
    def __init__(self):
        super().__init__("Wood", self.gold)

        
class Leather(Item): #Leather
    gold = 3
    
    def __init__(self):
        super().__init__("Leather", self.gold)

        
class Iron(Item): #Iron
    gold = 5 
    
    def __init__(self):
        super().__init__("Iron", self.gold)
    
    
class Gold(Item): #Gold
    gold = 20
    
    def __init__(self):
        super().__init__("Gold", self.gold)

        
class Sword(Item): #Sword
    gold = 800
    successCrafting = 5
    
    def __init__(self):
        super().__init__("Sword", self.gold)
    
    
    class Sword_Recipe(Recipes): #Sword recipe
        gold = 200

        def __init__(self):
            super().__init__("Sword Recipe", self.gold)
        
        def display(self):
            return super().display()
        
class Hammer(Item): #Hammer
    gold = 600
    successCrafting = 4
    
    def __init__(self):
        super().__init__("Hammer", self.gold)
    

    class Hammer_Recipe(Recipes): #Hammer recipe
        gold = 150

        def __init__(self):
            super().__init__("Hammer Recipe", self.gold)
        
        def display(self):
            return super().display()
        

class Bow(Item): #Bow
    gold = 400
    successCrafting = 3
    
    def __init__(self):
        super().__init__("Bow", self.gold)
    
    
    class Bow_Recipe(Recipes): #Bow recipe
        gold = 100

        def __init__(self):
            super().__init__("Bow Recipe", self.gold)
        
        def display(self):
            return super().display()
               
class Armor(Item):
    def __init__(self, name, gold):
        self.name = name
        self.gold = gold
        
class Helm(Armor): #Helm
    gold = 400
    successCrafting = 3
    
    def __init__(self):
        super().__init__("Helm", self.gold)

    
    class Helm_Recipe(Recipes): #Helm recipe
        gold = 100

        def __init__(self):
            super().__init__("Helm Recipe", self.gold)
        
        def display(self):
            return super().display()
             
class Chest(Armor): #Chest
    gold = 1000
    successCrafting = 6
    
    def __init__(self):
        super().__init__("Chest", self.gold)

    class Chest_Recipe(Recipes): #Chest recipe
        gold = 250

        def __init__(self):
            super().__init__("Chest Recipe", self.gold)
        
        def display(self):
            return super().display()
             
class Feet(Armor): #Feet
    gold = 300
    successCrafting = 3
    
    def __init__(self):
        super().__init__("Feet", self.gold)


    class Feet_Recipe(Recipes): #Feet recipe
        gold = 75

        def __init__(self):
            super().__init__("Feet Recipe", self.gold)
        
        def display(self):
            return super().display()
        
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
    sword_recipe = Sword.Sword_Recipe()
    hammer_recipe = Hammer.Hammer_Recipe()
    bow_recipe = Bow.Bow_Recipe()
    helm_recipe = Helm.Helm_Recipe()
    chest_recipe = Chest.Chest_Recipe()
    feet_recipe = Feet.Feet_Recipe()
    recipes = [sword_recipe,hammer_recipe,bow_recipe,helm_recipe,chest_recipe,feet_recipe]
    
    #The game will continue until the player has no gold or gets 100k
    while (player.gold > 0) and (player.gold <= 50000):
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
        
        print("\033[1;36mDay:\033[1;37m",day,"\n") #Print the current day
        
        command = input("\033[1;36mWhat do you wanna do in this day?\n" +
                        "\033[1;36m1. \033[1;37mBuy Items\n"+
                        "\033[1;36m2. \033[1;37mCraft Items\n"+
                        "\033[1;36m3. \033[1;37mSell items\n" +
                        "\033[1;36m4. \033[1;37mSee your inventory (This action will not occupy your day)\n")
        if command == "1": #Let the player buy things
            def shop():
                os.system('clear') #Clear the previous console information and messages
                print ("\033[1;36mGold: \033[1;33m" + str(player.gold) + "\n")
                command = input("\033[1;36mWhat do you wanna do?"+
                                "\n\033[1;36m1. \033[1;37mBuy resources" +
                                "\n\033[1;36m2. \033[1;37mBuy recipes (You can only buy 1 recipe per day!)\n")
                if command == "1": #Let the player buy resources
                    def buy_resources():
                        os.system('clear') #Clear the previous console information and messages
                        print ("\033[1;36mGold: \033[1;33m" + str(player.gold) + "\n")
                        command = input("\033[1;36m1. \033[1;37mWood: \033[1;33m" + str(myWood.gold) +
                                            "\n\033[1;36m2. \033[1;37mLeather: \033[1;33m" + str(myLeather.gold) +
                                            "\n\033[1;36m3. \033[1;37mIron: \033[1;33m" + str(myIron.gold) +
                                            "\n\033[1;36m4. \033[1;37mGold: \033[1;33m" + str(myGold.gold) + "\n" + 
                                            "\n\033[1;36mOr write 'B' to get back and end you day!\n")
                        if command == "1": #Buy wood
                            if player.gold >= myWood.gold:
                                player.gold -= myWood.gold
                                player.resources_inventory.append(myWood)
                                buy_resources() #Get back to the function if the player wants to buy more resources
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_resources() #Get back to the function if the player wants to buy more resources
                        elif command == "2": #Buy leather
                            if player.gold >= myLeather.gold:
                                player.gold -= myLeather.gold
                                player.resources_inventory.append(myLeather)
                                buy_resources() #Get back to the function if the player wants to buy more resources
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_resources() #Get back to the function if the player wants to buy more resources
                        elif command == "3": #Buy iron
                            if player.gold >= myIron.gold:
                                player.gold -= myIron.gold
                                player.resources_inventory.append(myIron)
                                buy_resources() #Get back to the function if the player wants to buy more resources
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_resources() #Get back to the function if the player wants to buy more resources
                        elif command == "4": #Buy gold
                            if player.gold >= myGold.gold:
                                player.gold -= myGold.gold
                                player.resources_inventory.append(myGold)
                                buy_resources() #Get back to the function if the player wants to buy more resources
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_resources() #Get back to the function if the player wants to buy more resources
                        elif command == "B":
                            pass
                        else:
                            print("\n\033[0;31mChoose a right action!")
                            print(input("\n\033[1;33mPress ENTER to continue!"))
                            buy_resources()
   
                    buy_resources() #Executes the function
                
                elif command == "2": #Let the player buy recipes
                    def buy_recipes():
                        os.system('clear') #Clear the previous console information and messages
                        print("\033[1;36mGold: \033[1;33m" + str(player.gold) + "\n")
                        command = input("\033[1;36m1. \033[1;37mSword recipe \033[1;33m" + str(sword_recipe.gold) +
                                        "\n\033[1;36m2. \033[1;37mHammer recipe: \033[1;33m" + str(hammer_recipe.gold) +
                                        "\n\033[1;36m3. \033[1;37mBow recipe: \033[1;33m" + str(bow_recipe.gold) +
                                        "\n\033[1;36m4. \033[1;37mHelm recipe: \033[1;33m" + str(helm_recipe.gold) + 
                                        "\n\033[1;36m5. \033[1;37mChest recipe: \033[1;33m" + str(chest_recipe.gold) + 
                                        "\n\033[1;36m6. \033[1;37mFeet recipe: \033[1;33m" + str(feet_recipe.gold) + "\n" +
                                        "\n\033[1;36mOr write 'B' to get back and end you day!\n")
                        if command == "1": #Buy sword recipe
                            if player.gold >= sword_recipe.gold:
                                player.gold -= sword_recipe.gold
                                player.items_inventory.append(sword_recipe)
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "2": #Buy Hammer recipe
                            if player.gold >= hammer_recipe.gold:
                                player.gold -= hammer_recipe.gold
                                player.items_inventory.append(hammer_recipe)
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "3": #Buy Bow recipe
                            if player.gold >= bow_recipe.gold:
                                player.gold -= bow_recipe.gold
                                player.items_inventory.append(bow_recipe)
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "4": #Buy Helm recipe
                            if player.gold >= helm_recipe.gold:
                                player.gold -= helm_recipe.gold
                                player.items_inventory.append(helm_recipe)
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "5": #Chest recipe
                            if player.gold >= chest_recipe.gold:
                                player.gold -= chest_recipe.gold
                                player.items_inventory.append(chest_recipe)
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "6": #Buy Feet recipe
                            if player.gold >= feet_recipe.gold:
                                player.gold -= feet_recipe.gold
                                player.items_inventory.append(feet_recipe)
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "B":
                            pass
                        else:
                            print("\n\033[0;31mChoose a right action!")
                            print(input("\n\033[1;33mPress ENTER to continue!"))
                            buy_recipes() #Get back to the recipes buy menu
                        
                    buy_recipes() #Start the function
                    
                else:
                    print("\n\033[0;31mChoose a right action!")
                    print(input("\n\033[1;33mPress ENTER to continue"))
                    shop()
            
            shop()
            
        elif command == "2": #Let the player craft items
            def crafting():
                os.system('clear') #Clear the previous console information and messages
                if sword_recipe in player.items_inventory:
                        print("\033[0;36m1. \033[1;37mSword (Needed: 2 Woods and 3 Irons)")
                if hammer_recipe in player.items_inventory:
                        print("\033[0;36m2. \033[1;37mHammer (Needed: 2 Woods and 4 Irons)")
                if bow_recipe in player.items_inventory:
                        print("\033[0;36m3. \033[1;37mBow (Needed: 5 Woods, 1 Iron and 2 Leathers)")
                if helm_recipe in player.items_inventory:
                        print("\033[0;36m4. \033[1;37mHelm (Needed: 3 Irons and 1 Gold)")
                if chest_recipe in player.items_inventory:
                        print("\033[0;36m5. \033[1;37mChest (Needed: 5 Irons and 2 Golds)")
                if feet_recipe in player.items_inventory:
                        print("\033[0;36m6. \033[1;37mFeet (Needed: 2 Irons and 2 Golds)")
                        
                #Check if any recipe is in the player's inventory
                checkRecipes = any(n in recipes for n in player.items_inventory)
                if checkRecipes is False:
                    print("\033[0;31mYou need a recipe to craft something!")
                    print(input("\n\033[1;33mPress ENTER to continue"))
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
                            print("\n\033[0;32mYou have crafted a sword!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                        if playerCraftAttempt < sword.successCrafting: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a sword!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31mYou don't have all the materials to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                            
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
                            print("\n\033[0;32mYou have crafted a hammer!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < hammer.successCrafting: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a hammer!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31mYou don't have all the materials to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))

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
                            print("\n\033[0;32mYou have crafted a bow!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                        if playerCraftAttempt < bow.successCrafting: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a bow!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31mYou don't have all the materials to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                        
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
                            print("\n\033[0;32mYou have crafted a helm!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < helm.successCrafting: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a helm!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31mYou don't have all the materials to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))

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
                            print("\n\033[0;32mYou have crafted a chest!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < chest.successCrafting: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a chest!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31mYou don't have all the materials to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                        
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
                            print("\n\033[0;32mYou have crafted a feet!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < feet.successCrafting: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a feet!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31m\033[0;31mYou don't have all the materials to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                
                def choose_craft(): #Let the player select what we wants to craft
                    print("\n\033[0;37mOr write 'B' to get back home. (You will lose your day)")
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
                        print("\033[0;31mChoose a right action!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                        crafting()
                
                if checkRecipes is True:
                    choose_craft()
                    
            crafting()
                        
        elif command == "3": #Let the player sell his items
            os.system('clear') #Clear the previous console information and messages
            clients = random.randint(0,player.experience) #Random number of clients per day, more experience can get more clients
            sellable_items = [sword,hammer,bow,helm,chest,feet]
            items = [] #Sellable items in the player's inventory
            for i in sellable_items:
                if i in player.items_inventory:
                    items.append(i)
    
            def offer(): #Client offer
                if any(items):
                    client_choice = random.choice(items) #Item that the client is going to choose
                    client_offer = client_choice.gold * random.uniform(0.7,1.3) #Initial client's offer
                    def proposal_decision(): #Initial offer from the client
                        if client_choice in player.items_inventory: #Check if the item is in the player's inventory
                            os.system('clear') #Clear the previous console information and messages
                            print("\033[0;36mClient: \033[0;37mI offer you this - \033[0;33m" + str(round(client_offer))  + " \033[0;37mGold - " + "\033[0;36mfor: \033[0;37m" + client_choice.name)
                            command = input("\n\033[0;36mDo you want to accept it? (Y/N)\n")
                            if command == "Y": #If the player accepts it then:
                                player.gold += round(client_offer)
                                print("\n\033[0;36mCurrent Gold:\033[0;37m",player.gold)
                                player.items_inventory.remove(client_choice)
                                print(input("\n\033[1;33mPress ENTER to continue"))
                            elif command == "N": #If the player refuses then:
                                def bargain(): #Negotiate a new deal
                                    command = input("\n\033[0;36mDo you want to bargain? (Y/N)\n")
                                    if command == "Y": #If the player wants to negotiate:
                                        threshold = client_offer * random.uniform(1,1.3)
                                        round(threshold)
                                        def player_offer():
                                            counter_offer = input("\n\033[0;36mMake your offer: ")
                                            try:
                                                counter_offer = int(counter_offer)
                                                if (counter_offer < threshold):
                                                    player.gold += round(counter_offer)
                                                    print("\n\033[0;32mThe client has accepted your offer.")
                                                    print("\n\033[0;36mCurrent Gold:\033[1;33m",player.gold)
                                                    player.items_inventory.remove(client_choice)
                                                    print(input("\n\033[1;33mPress ENTER to continue"))
                                                else:
                                                    print("\n\033[0;31mThe customer refused your offer and left.")
                                                    print(input("\n\033[1;33mPress ENTER to continue"))
                                            except ValueError:
                                                print('\n\033[0;31mThe provided value is not a number!')
                                                print(input("\n\033[1;33mPress ENTER to continue"))
                                                player_offer()
                                            
                                        player_offer()
                                    elif command == "N": #If the player does not wants to negotiate:
                                        pass
                                    else: 
                                        print("\n\033[0;31mChoose a right action!")
                                        print(input("\n\033[1;33mPress ENTER to continue"))
                                        bargain()
                                bargain()
                            else:
                                print("\n\033[0;31mChoose a right action!")
                                print(input("\n\033[1;33mPress ENTER to continue"))
                                proposal_decision()
                        else:
                            pass
                        
                    proposal_decision() #Executes proposal
            
                return items
                    
            def selling_items(items): #Selling items
                if (clients > 0) and (any(items)): #If there's client on the shop:
                    for i in range(clients):
                        if any(items):
                            offer()
                        else:
                            pass
                    os.system('clear') #Clear the previous console information and messages
                    if any(items):
                        print("\033[1;37mYou have no more clients today!")
                        print(input("\n\033[1;33mPress ENTER to get back to the main menu"))
                        
                elif not items: #If the player got nothing to sell
                    os.system('clear') #Clear the previous console information and messages
                    print("\033[1;31mYou have got nothing to sell!")
                    print(input("\n\033[1;33mPress ENTER to get back to the main menu"))
                
                elif clients == 0: #If there's no clients on the shop:
                    print("\033[1;37mYou have no clients today.")
                    print(input("\n\033[1;33mPress ENTER to get back to the main menu"))
            
            selling_items(items) #Execute the function to sell items
        
        elif command == "4": #Show to the player his inventory
            os.system('clear') #Clear the previous console information and messages
            day -= 1
            print("\033[0;36mGold:\033[1;33m",player.gold)
            print("\33[0;37m-------")
            print("\033[0;36mPlayer level:\033[0;32m",player.experience)
            print("\33[0;37m-------")
            print("\033[0;35mResources:\33[0;37m\n"+
                  "\033[0;36mWood: \33[0;37m" + str(woodInInventory) + " /" + 
                  " \033[0;36mLeather: \33[0;37m" + str(leatherInInventory) + " /" +
                  " \033[0;36mIron: \33[0;37m" + str(ironInInventory) + " /" +
                  " \033[0;36mGold: \33[0;37m" + str(goldInInventory))
            print("-------")
            for item in player.items_inventory:
                item.display()
                print("\33[0;37m-------")
            print(input("\n\n\033[1;33mPress ENTER to get back to the main menu"))
            if command == "":
                pass
        else:
            day -= 1
            print("\n\033[0;31mChoose a right action!")
            print(input("\n\033[1;33mPress ENTER to continue"))
            pass

game_loop(day)