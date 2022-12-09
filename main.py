import os #Let he work with operating system functions
import random #Random library - can set random numbers

os.system('clear') #Clear the previous console information and messages

#Game explanation
print("\033[1;37mIn this game you must get up to 50k in gold to win, by buying resources, crafting items and after selling them, or if you lose all your money you lose.")
print(input("\n\033[1;33mPress ENTER to continue"))
os.system('clear') #Clear the previous console information and messages

#variables
day = 0

#Inventory and items
class Player:
    gold = 500
    experience = 1
    resources_inventory = []
    items_inventory = []
    
class Item:
    def __init__(self,name,gold,successCraft):
        self.name = name
        self.gold = gold
        self.successCraft = successCraft
    
    def display(self):
        print("\033[0;36mItem:\033[1;37m", self.name)
        print("\033[0;36mAverage selling price:\033[1;33m", self.gold)
        
class Resources(Item): #Resources Class
    def __init__(self,name,gold):
        self.name = name
        self.gold = gold
        
class Recipes: #Recipes Class
    def __init__(self,name,gold):
        self.name = name
        self.gold = gold
    
    def display(self):
        print("\033[0;36mItem:\033[1;37m", self.name)
        
class Armor(Item): #Armor class
    def __init__(self, name, gold, successCraft):
        self.name = name
        self.gold = gold
        self.successCraft = successCraft

class Wood(Resources): #Wood
    def __init__(self):
        super().__init__("Wood", 2)

        
class Leather(Resources): #Leather
    def __init__(self):
        super().__init__("Leather", 3)

        
class Iron(Resources): #Iron
    def __init__(self):
        super().__init__("Iron", 5)
    
    
class Gold(Resources): #Gold
    def __init__(self):
        super().__init__("Gold", 20)

        
class Sword(Item): #Sword
    def __init__(self):
        super().__init__("Sword", 800, 5)
    
    class Sword_Recipe(Recipes): #Sword recipe
        def __init__(self):
            super().__init__("Sword Recipe", 200)
        
class Hammer(Item): #Hammer
    def __init__(self):
        super().__init__("Hammer", 600, 4)
    

    class Hammer_Recipe(Recipes): #Hammer recipe
        def __init__(self):
            super().__init__("Hammer Recipe", 150)
        

class Bow(Item): #Bow
    def __init__(self):
        super().__init__("Bow", 400, 3)
    
    
    class Bow_Recipe(Recipes): #Bow recipe
        def __init__(self):
            super().__init__("Bow Recipe", 100)
        
class Gem(Item): #Gem
    def __init__(self):
        super().__init__("Gem", 350, 2)
    
    class Gem_Recipe(Recipes): #Gem recipe
        def __init__(self):
            super().__init__("Gem Recipe", 100)
            
class Pickaxe(Item): #Pickaxe
    def __init__(self):
        super().__init__("Pickaxe", 450, 3)
    
    class Pickaxe_Recipe(Recipes): #Pickaxe recipe
        def __init__(self):
            super().__init__("Pickaxe Recipe", 135)

class Axe(Item): #Axe
    def __init__(self):
        super().__init__("Axe", 550, 4)
    
    class Axe_Recipe(Recipes): #Axe recipe
        def __init__(self):
            super().__init__("Axe Recipe", 180)

class Shield(Item): #Shield
    def __init__(self):
        super().__init__("Shield", 300, 2)
    
    class Shield_Recipe(Recipes): #Shield recipe
        def __init__(self):
            super().__init__("Shield Recipe", 80)

class Fishing_Rod(Item): #Fishing rod
    def __init__(self):
        super().__init__("Fishing Rod", 250, 1)
        
    class Fishing_Rod_Recipe(Recipes): #Fishing rod recipe
        def __init__(self):
            super().__init__("Fishing Rod Recipe", 50)

class Wizard_Book(Item): #Wizard Book
    def __init__(self):
        super().__init__("Wizard Book", 1500, 8)
    
    class Wizard_Book_Recipe(Recipes): #Wizard Book recipe
        def __init__(self):
            super().__init__("Wizard Book Recipe", 300)

class Vault(Item): #Vault
    def __init__(self):
        super().__init__("Vault", 350, 2)
        
    class Vault_Recipe(Recipes): #Vault Recipe
        def __init__(self):
            super().__init__("Vault Recipe", 125)

class Shuriken(Item): #Shuriken
    def __init__(self):
        super().__init__("Shuriken", 500, 3)
    
    class Shuriken_Recipe(Recipes): #Shuriken Recipe
        def __init__(self):
            super().__init__("Shuriken Recipe", 160)

class Nunchucks(Item): #Nunchucks
    def __init__(self):
        super().__init__("Nunchucks", 700, 4)
    
    class Nunchucks_Recipe(Recipes): #Nunchuks recipe
        def __init__(self):
            super().__init__("Nunchucks Recipe", 190)
        
class Helm(Armor): #Helm
    def __init__(self):
        super().__init__("Helm", 400, 3)
    
    class Helm_Recipe(Recipes): #Helm recipe
        def __init__(self):
            super().__init__("Helm Recipe", 100)
             
class Chest(Armor): #Chest
    def __init__(self):
        super().__init__("Chest", 1000, 6)

    class Chest_Recipe(Recipes): #Chest recipe
        def __init__(self):
            super().__init__("Chest Recipe", 250)
             
class Feet(Armor): #Feet
    def __init__(self):
        super().__init__("Feet", 300, 3)

    class Feet_Recipe(Recipes): #Feet recipe
        def __init__(self):
            super().__init__("Feet Recipe", 75)
        
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
    gem = Gem()
    pickaxe = Pickaxe()
    axe = Axe()
    shield = Shield()
    fishing_rod = Fishing_Rod()
    wizard_book = Wizard_Book()
    vault = Vault()
    shuriken = Shuriken()
    nunchucks = Nunchucks()
    sword_recipe = Sword.Sword_Recipe()
    hammer_recipe = Hammer.Hammer_Recipe()
    bow_recipe = Bow.Bow_Recipe()
    helm_recipe = Helm.Helm_Recipe()
    chest_recipe = Chest.Chest_Recipe()
    feet_recipe = Feet.Feet_Recipe()
    gem_recipe = Gem.Gem_Recipe()
    axe_recipe = Axe.Axe_Recipe()
    shield_recipe = Shield.Shield_Recipe()
    pickaxe_recipe = Pickaxe.Pickaxe_Recipe()
    fishing_rod_recipe = Fishing_Rod.Fishing_Rod_Recipe()
    wizard_book_recipe = Wizard_Book.Wizard_Book_Recipe()
    vault_recipe = Vault.Vault_Recipe()
    shuriken_recipe = Shuriken.Shuriken_Recipe()
    nunchucks_recipe = Nunchucks.Nunchucks_Recipe()
    
    #Recipes list
    recipes = [sword_recipe,hammer_recipe,bow_recipe,helm_recipe,chest_recipe,feet_recipe,gem_recipe,pickaxe_recipe,axe_recipe,shield_recipe,fishing_rod_recipe,wizard_book_recipe,vault_recipe,shuriken_recipe,nunchucks_recipe]
    
    #The game will continue until the player has no gold or gets 50k
    while (player.gold > 0) and (player.gold < 50000):
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
        
        command = input("\033[1;36mWhat you want to do on this day?\n" +
                        "\033[1;36m1. \033[1;37mBuy Resources/Recipes\n"+
                        "\033[1;36m2. \033[1;37mCraft Items\n"+
                        "\033[1;36m3. \033[1;37mSell items\n" +
                        "\033[1;36m4. \033[1;37mSee your inventory (This action will not occupy your day)\n\033[1;37m")
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
                                            "\n\033[1;36mOr write 'B' to get back home and end you day!\n\033[1;37m")
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
                                        "\n\033[1;36m6. \033[1;37mFeet recipe: \033[1;33m" + str(feet_recipe.gold) +
                                        "\n\033[1;36m7. \033[1;37mGem recipe: \033[1;33m" + str(gem_recipe.gold) +
                                        "\n\033[1;36m8. \033[1;37mPickaxe recipe: \033[1;33m" + str(pickaxe_recipe.gold) +
                                        "\n\033[1;36m9. \033[1;37mAxe recipe: \033[1;33m" + str(axe_recipe.gold) +
                                        "\n\033[1;36m10. \033[1;37mShield recipe: \033[1;33m" + str(shield_recipe.gold) +
                                        "\n\033[1;36m11. \033[1;37mFishing Rod recipe: \033[1;33m" + str(fishing_rod_recipe.gold) +
                                        "\n\033[1;36m12. \033[1;37mWizard Book recipe: \033[1;33m" + str(wizard_book_recipe.gold) +
                                        "\n\033[1;36m13. \033[1;37mVault recipe: \033[1;33m" + str(vault_recipe.gold) +
                                        "\n\033[1;36m14. \033[1;37mShuriken recipe: \033[1;33m" + str(shuriken_recipe.gold) +
                                        "\n\033[1;36m15. \033[1;37mNunchucks recipe: \033[1;33m" + str(nunchucks_recipe.gold) +
                                        "\n\n\033[1;36mOr write 'B' to get back home and end you day!\n\033[1;37m")
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
                        elif command == "7": #Buy Gem recipe
                            if player.gold >= gem_recipe.gold:
                                player.gold -= gem_recipe.gold
                                player.items_inventory.append(gem_recipe)
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "8": #Buy pickaxe recipe
                            if player.gold >= pickaxe_recipe.gold:
                                player.gold -= pickaxe_recipe.gold
                                player.items_inventory.append(pickaxe_recipe)
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "9": #Buy axe recipe
                            if player.gold >= axe_recipe.gold:
                                player.gold -= axe_recipe.gold
                                player.items_inventory.append(axe_recipe)
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "10": #Buy shield recipe
                            if player.gold >= shield_recipe.gold:
                                player.gold -= shield_recipe.gold
                                player.items_inventory.append(shield_recipe)
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "11": #Buy fishing rod recipe
                            if player.gold >= fishing_rod_recipe.gold:
                                player.gold -= fishing_rod_recipe.gold
                                player.items_inventory.append(fishing_rod_recipe)
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "12": #Buy wizard book recipe
                            if player.gold >= wizard_book_recipe.gold:
                                player.gold -= wizard_book_recipe.gold
                                player.items_inventory.append(wizard_book_recipe)
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "13": #Buy vault recipe
                            if player.gold >= vault_recipe.gold:
                                player.gold -= vault_recipe.gold
                                player.items_inventory.append(vault_recipe)
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "14": #Buy shuriken recipe
                            if player.gold >= shuriken_recipe.gold:
                                player.gold -= shuriken_recipe.gold
                                player.items_inventory.append(shuriken_recipe)
                            else:
                                print("\n\033[1;31mYou do not have enough gold to buy this!")
                                print(input("\n\033[1;33mPress ENTER to continue!"))
                                buy_recipes() #Get back to the recipes buy menu
                        elif command == "15": #Buy nunchucks recipe
                            if player.gold >= nunchucks_recipe.gold:
                                player.gold -= nunchucks_recipe.gold
                                player.items_inventory.append(nunchucks_recipe)
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
                if gem_recipe in player.items_inventory:
                    print("\033[0;36m7. \033[1;37mGem (Needed: 4 Irons and 4 Golds)")
                if pickaxe_recipe in player.items_inventory:
                    print("\033[0;36m8. \033[1;37mPickaxe (Needed: 2 Woods and 3 Irons)")
                if axe_recipe in player.items_inventory:
                    print("\033[0;36m9. \033[1;37mAxe (Needed: 2 Woods and 4 Irons)")
                if shield_recipe in player.items_inventory:
                    print("\033[0;36m10. \033[1;37mShield (Needed: 3 Woods and 3 Irons)")
                if fishing_rod_recipe in player.items_inventory:
                    print("\033[0;36m11. \033[1;37mFishing Rod (Needed: 5 Woods and 2 Leathers)")
                if wizard_book_recipe in player.items_inventory:
                    print("\033[0;36m12. \033[1;37mWizard Book (Needed: 2 Woods and 6 Leathers)")
                if vault_recipe in player.items_inventory:
                    print("\033[0;36m13. \033[1;37mVault (Needed: 8 Irons)")
                if shuriken_recipe in player.items_inventory:
                    print("\033[0;36m14. \033[1;37mShuriken (Needed: 2 Irons)")
                if nunchucks_recipe in player.items_inventory:
                    print("\033[0;36m15. \033[1;37mNunchucks (Needed: 2 Woods and 4 Irons)")
                        
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
                        if playerCraftAttempt >= sword.successCraft: #Success craft attempt
                            player.items_inventory.append(sword)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a sword!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                        if playerCraftAttempt < sword.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a sword!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31mYou don't have all the materials needed to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                            
                def hammer_craft(): #Craft hammer
                    if int(woodInInventory) >= 2 and int(ironInInventory) >= 4: #If the player got the materials to craft then:
                        hammer_materials = [myWood,myWood,myIron,myIron,myIron,myIron] #Materials needed to do the hammer
                        for materials in hammer_materials: #Remove the materials needed to do the hammer
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(hammer_recipe)
                        if playerCraftAttempt >= hammer.successCraft: #Success craft attempt
                            player.items_inventory.append(hammer)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a hammer!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < hammer.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a hammer!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31mYou don't have all the materials needed to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))

                def bow_craft(): #Craft bow
                    if int(woodInInventory) >= 5 and int(ironInInventory) >= 1 and int(leatherInInventory) >= 2: #If the player got the materials to craft then:
                        bow_materials = [myWood,myWood,myWood,myWood,myWood,ironInInventory,leatherInInventory, leatherInInventory] #Materials needed to do the bow
                        for materials in bow_materials: #Remove the materials needed to do the bow
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(bow_recipe)
                        if playerCraftAttempt >= bow.successCraft: #Success craft attempt
                            player.items_inventory.append(bow)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a bow!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                        if playerCraftAttempt < bow.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a bow!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31mYou don't have all the materials needed to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                        
                def helm_craft(): #Craft helm
                    if int(ironInInventory) >= 3 and int(goldInInventory) >= 1: #If the player got the materials to craft then:
                        helm_materials = [myIron,myIron,myIron,myGold] #Materials needed to do the helm
                        for materials in helm_materials: #Remove the materials needed to do the helm
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(helm_recipe)
                        if playerCraftAttempt >= helm.successCraft: #Success craft attempt
                            player.items_inventory.append(helm)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a helm!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < helm.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a helm!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31mYou don't have all the materials needed to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))

                def chest_craft(): #Craft chest
                    if int(ironInInventory) >= 5 and int(goldInInventory) >= 2: #If the player got the materials to craft then:
                        chest_materials = [myIron,myIron,myIron,myIron,myIron,myGold,myGold] #Materials needed to do the chest
                        for materials in chest_materials: #Remove the materials needed to do the chest
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(chest_recipe)
                        if playerCraftAttempt >= chest.successCraft: #Success craft attempt
                            player.items_inventory.append(chest)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a chest!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < chest.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a chest!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31mYou don't have all the materials needed to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                        
                def feet_craft(): #Craft feet
                    if int(ironInInventory) >= 2 and int(goldInInventory) >= 2: #If the player got the materials to craft then:
                        feet_materials = [myIron,myIron,myGold,myGold] #Materials needed to do the feet
                        for materials in feet_materials: #Remove the materials needed to do the feet
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(feet_recipe)
                        if playerCraftAttempt >= feet.successCraft: #Success craft attempt
                            player.items_inventory.append(feet)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a feet!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < feet.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a feet!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31m\033[0;31mYou don't have all the materials needed to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                        
                def gem_craft(): #Craft gem
                    if int(ironInInventory) >= 4 and int(goldInInventory) >= 4: #If the player got the materials to craft then:
                        gem_materials = [myIron,myIron,myIron,myIron,myGold,myGold,myGold,myGold] #Materials needed to do the gem
                        for materials in gem_materials: #Remove the materials needed to do the gem
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(gem_recipe)
                        if playerCraftAttempt >= gem.successCraft: #Success craft attempt
                            player.items_inventory.append(gem)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a gem!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < gem.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a gem!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31m\033[0;31mYou don't have all the materials needed to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                
                def pickaxe_craft(): #Craft pickaxe
                    if int(ironInInventory) >= 3 and int(woodInInventory) >= 2: #If the player got the materials to craft then:
                        pickaxe_materials = [myIron,myIron,myIron,myWood,myWood] #Materials needed to do the pickaxe
                        for materials in pickaxe_materials: #Remove the materials needed to do the pickaxe
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(pickaxe_recipe)
                        if playerCraftAttempt >= pickaxe.successCraft: #Success craft attempt
                            player.items_inventory.append(pickaxe)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a pickaxe!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < pickaxe.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a pickaxe!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31m\033[0;31mYou don't have all the materials needed to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                
                def axe_craft(): #Craft axe
                    if int(ironInInventory) >= 4 and int(woodInInventory) >= 2: #If the player got the materials to craft then:
                        axe_materials = [myIron,myIron,myIron,myIron,myWood,myWood] #Materials needed to do the axe
                        for materials in axe_materials: #Remove the materials needed to do the axe
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(axe_recipe)
                        if playerCraftAttempt >= axe.successCraft: #Success craft attempt
                            player.items_inventory.append(axe)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a axe!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < axe.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a axe!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                
                def shield_craft(): #Craft shield
                    if int(ironInInventory) >= 3 and int(woodInInventory) >= 3: #If the player got the materials to craft then:
                        shield_materials = [myIron,myIron,myIron,myWood,myWood,myWood] #Materials needed to do the shield
                        for materials in shield_materials: #Remove the materials needed to do the shield
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(shield_recipe)
                        if playerCraftAttempt >= shield.successCraft: #Success craft attempt
                            player.items_inventory.append(shield)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a shield!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < shield.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a shield!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31m\033[0;31mYou don't have all the materials needed to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                
                def fishing_rod_craft(): #Craft fishing rod
                    if int(woodInInventory) >= 5 and int(leatherInInventory) >= 2: #If the player got the materials to craft then:
                        fishing_rod_materials = [myWood,myWood,myWood,myWood,myWood,myLeather,myLeather] #Materials needed to do the fishing rod
                        for materials in fishing_rod_materials: #Remove the materials needed to do the fishing rod
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(fishing_rod_recipe)
                        if playerCraftAttempt >= fishing_rod.successCraft: #Success craft attempt
                            player.items_inventory.append(fishing_rod)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a fishing rod!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < fishing_rod.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a fishing rod!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31m\033[0;31mYou don't have all the materials needed to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                
                def wizard_book_craft(): #Craft wizard_book
                    if int(woodInInventory) >= 2 and int(leatherInInventory) >= 6: #If the player got the materials to craft then:
                        wizard_book_materials = [myWood,myWood,myLeather,myLeather,myLeather,myLeather,myLeather,myLeather] #Materials needed to do the wizard book
                        for materials in wizard_book_materials: #Remove the materials needed to do the wizard book
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(wizard_book_recipe)
                        if playerCraftAttempt >= wizard_book.successCraft: #Success craft attempt
                            player.items_inventory.append(wizard_book)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a wizard book!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < wizard_book.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a wizard book!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31m\033[0;31mYou don't have all the materials needed to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                
                def vault_craft(): #Craft vault
                    if int(ironInInventory) >= 8: #If the player got the materials to craft then:
                        vault_materials = [myIron,myIron,myIron,myIron,myIron,myIron,myIron,myIron] #Materials needed to do the vault
                        for materials in vault_materials: #Remove the materials needed to do the vault
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(vault_recipe)
                        if playerCraftAttempt >= vault.successCraft: #Success craft attempt
                            player.items_inventory.append(vault)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a vault!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < vault.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a vault!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31m\033[0;31mYou don't have all the materials needed to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                
                def shuriken_craft(): #Craft shuriken
                    if int(ironInInventory) >= 2 : #If the player got the materials to craft then:
                        shuriken_materials = [myIron,myIron] #Materials needed to do the shuriken
                        for materials in shuriken_materials: #Remove the materials needed to do the shuriken
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(shuriken_recipe)
                        if playerCraftAttempt >= shuriken.successCraft: #Success craft attempt
                            player.items_inventory.append(shuriken)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a shuriken!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < shuriken.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a shuriken!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31m\033[0;31mYou don't have all the materials needed to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                
                def nunchucks_craft(): #Craft nunchucks
                    if int(ironInInventory) >= 4 and int(woodInInventory) >= 2: #If the player got the materials to craft then:
                        nunchucks_materials = [myIron,myIron,myIron,myIron,myWood,myWood] #Materials needed to do the nunchucks
                        for materials in nunchucks_materials: #Remove the materials needed to do the nunchucks
                            if materials in player.resources_inventory:
                                player.resources_inventory.remove(materials)
                        player.items_inventory.remove(nunchucks_recipe)
                        if playerCraftAttempt >= nunchucks.successCraft: #Success craft attempt
                            player.items_inventory.append(nunchucks)
                            player.experience += 1
                            print("\n\033[0;32mYou have crafted a nunchucks!")
                            print(input("\n\033[1;33mPress ENTER to continue"))  
                        if playerCraftAttempt < nunchucks.successCraft: #Failed craft attempt
                            print("\n\033[0;31mYou have failed to craft a nunchucks!")
                            print(input("\n\033[1;33mPress ENTER to continue"))
                    else:
                        print("\n\033[0;31m\033[0;31mYou don't have all the materials needed to craft this!")
                        print(input("\n\033[1;33mPress ENTER to continue"))
                
                def choose_craft(): #Let the player select what we wants to craft
                    print("\n\033[0;37mOr write 'B' to get back home. (You will lose your day)\033[1;37m")
                    command = input("\033[1;37m")
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
                    elif (command == "7") and (gem_recipe in player.items_inventory):
                            gem_craft()
                    elif (command == "8") and (pickaxe_recipe in player.items_inventory):
                            pickaxe_craft()
                    elif (command == "9") and (axe_recipe in player.items_inventory):
                            axe_craft()
                    elif (command == "10") and (shield_recipe in player.items_inventory):
                            shield_craft()
                    elif (command == "11") and (fishing_rod_recipe in player.items_inventory):
                            fishing_rod_craft()
                    elif (command == "12") and (wizard_book_recipe in player.items_inventory):
                            wizard_book_craft()
                    elif (command == "13") and (vault_recipe in player.items_inventory):
                            vault_craft()
                    elif (command == "14") and (shuriken_recipe in player.items_inventory):
                            shuriken_craft()
                    elif (command == "15") and (nunchucks_recipe in player.items_inventory):
                            nunchucks_craft()
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
            sellable_items = [sword,hammer,bow,helm,chest,feet,gem,pickaxe,axe,shield,fishing_rod,wizard_book,vault,shuriken,nunchucks]
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
                            command = input("\n\033[0;36mDo you want to accept it? (Y/N)\n\033[1;37m")
                            if command == "Y": #If the player accepts it then:
                                player.gold += round(client_offer)
                                print("\n\033[0;36mCurrent Gold:\033[0;37m",player.gold)
                                player.items_inventory.remove(client_choice)
                                print(input("\n\033[1;33mPress ENTER to continue"))
                            elif command == "N": #If the player refuses then:
                                def bargain(): #Negotiate a new deal
                                    command = input("\n\033[0;36mDo you want to bargain? (Y/N)\n\033[1;37m")
                                    if command == "Y": #If the player wants to negotiate:
                                        threshold = client_offer * random.uniform(1,1.1)
                                        round(threshold)
                                        def player_offer():
                                            counter_offer = input("\n\033[0;36mMake your offer: \033[1;37m")
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
    if player.gold <= 0: #If the player loses all his money
        os.system('clear') #Clear the previous console information and messages
        print("\033[0;31mYou lost all your money and became homeless! Better luck next time.")
    if player.gold >= 50000: #If the player get to 50k
        os.system('clear') #Clear the previous console information and messages
        print("\033[0;32mYou made 50k and went to live in the Bahamas! Well played!")

game_loop(day)