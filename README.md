# mini-project-1-fudamentals-of-programming

# FP1 - Mini Project 1

### Objective of the Project:

Implement the described dealer system with options to buy resources, craft item, and sell them.
## Developers

- [@Rafael-j-03](https://github.com/Rafael-j-03)
- [@rodgoe](https://github.com/rodgoe)
## How our project was organized

- The code production was mostly done by Rafael José, Rodrigo Gomes also contributed to it, helping to solve some problems and some logical systems.
The README.md was mostly done by Rodrigo Gomes, in which Rafael José helped composed some more information.
- 1st commit - First version of the main menu, which contained some preset items, and the 3 options do "Buy resources", "Craft Items" and "Sell Items". - Rafael José - 22202078

- 2nd commit - Implementation of the system to buy resources, and some alterations in the classes from the items, new class "Player" with the player's gold, player's resources inventory and player's items inventory. - Rafael José - 22202078

- 3rd commit - Let the player buy the recipes, and new method of player experience. - Rafael José - 22202078

- 4th commit- The price of the recipes no longer appears in the inventory, as it is an item that cannot be sold. - Rafael José - 22202078

- 5th commit - Beta Crafting System (Only up to the sword). - Rafael José - 22202078

- 6th commit - Craft system finish. - Rafael José - 22202078

- 7th commit- Beta item selling. - Rafael José - 22202078

- 8th commit - Selling system finish - Rafael José - 22202078

- 9th commit - Some dead rode removal and added some colors to the prints. - Rafael José - 22202078

- 10th commit - New items and recipes added and code clear. - Rafael José - 22202078

- 11th commit - Corrected and added some notes. - Rafael José - 22202078

- 12th - Implementation of the README.md - Rodrigo Gomes - 22201252

[Git Repository](https://github.com/Rafael-j-03/IC-Project)
## Development of our work

### How we organized our code

- We first created a simple explanation of the game to show the player what he needs to do.

- After we created a menu, that lets the player chooses the action that he will do on that day, the player can only do an action per day, except going to the inventory.

- The first option, of the menu, lets the player buy resources or recipes, the player can buy multiple resource in a day, but only can only buy 1 recipe per day. After the purchase if the player decides to buy resources, they will go to the player's resources inventory, where they will be stacked by resources, if the player wants to buy a recipe it will go the player's items inventory.

- The second option is a system to craft items, where the player needs to have the proper recipe and the proper resources to craft an item that he wants to craft. If the player has all he needs to craft the item (the resources and the proper recipe), then he has a chance to get the crafting done or not, either way the player will lose the resources and the recipe he chooses to craft. After each craft completed the item that the player wanted to craft will be append on the player's items inventory, the player will also win +1 experience, which will raise him 1 level.

- The third option is a system to sell the items that the player have crafted, in this step the player will get a random number of clients in his shop, the number will randomize from 0 to the level of the player, each client will do an offer for a random item, depending on the item that the client chooses the price will rise or lower randomly (the average selling price from each item is showed in the next option), the player can then accept the client's offer, or deny it and try to sell it for the price he wants, the client will check if he agrees with the price, and tell if it is a deal or not. If the player sells the item, the item is goning to leave the inventory.

- The fourth and last option, is letting the player see what he has on the inventory, combining the resources inventory and the items inventory. The resources inventory will appear stack by each resource, including if the player has 0 from the that resource, the items from the items inventory will appear one by one, if the item can be sold it will appear the name from the item and its average selling price, if the items can't be sold its name will appear, in this case the recipes.

## References

- We import two external libraries, os and random.
  
- The "random" like the article about it says "This module implements pseudo-random number generators for various distributions.
For integers, there is a uniform selection from a range. For sequences, there is a uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.". And we used it to get random numbers mostly for the dices system.

- The "os" like the article about it says "This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see open(), if you want to manipulate paths, see the os.path module, and if you want to read all the lines in all the files on the command line see the fileinput module. For creating temporary files and directories see the tempfile module, and for high-level file and directory handling see the shutil module.". We used it just to clear the console of the player before the start of a new round, to get a better view of the game.
