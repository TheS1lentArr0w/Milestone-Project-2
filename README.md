# Milestone-Project-2
This is the second milestone project that I completed during my [Python Bootcamp](https://www.udemy.com/course/complete-python-bootcamp/).

It is a simplified text version of BlackJack.

Compared to my [first milestone project](https://github.com/TheS1lentArr0w/Milestone-Project-1), I decided not to follow the Code-Along file and decided to take this 
project on myself.

The main skill that is displayed with this project is OOP (Object Oriented Programming).

## Programming Language and IDE
This project was coded using Python in Sublime Text 4.

## Project Description
There is one human player and one computer dealer. The player has an attribute, "bank roll", which acts as the player's chips. The player starts with 1000 and the minimum
is 100 to play.

Once the cards are dealt from the deck, the player has 2 face up cards and the dealer has 1 card face up and 1 card face down. From here, the player can either 
hit or stay. This loop continues until the player either stays or busts.

After the player's turn concludes, the dealer hits until their total value is >= 17. This includes the dealer going bust.

After both the player and the dealers' turns have ended, the total values of their hands are compared. If the player wins, the player earns double their bet (e.g. if 
the player bet 100 and they win, the player earns 200). If the dealer wins, the bet is taken away from the player's bankroll. If it is a draw, the bet returns to the 
player.

Finally, the player can decide whether they want to keep playing or not.

## Challenges
The main challenge that I came across during this project was how to handle Aces, which could either be 1 or 11. Initially, my idea was to give the human player a choice of whether the Ace in their hand has the value of 1 or 11. However, I could not figure out how to efficiently code this in. I researched for a solution instead and came across this on [Stack Overflow](https://stackoverflow.com/questions/46088655/manipulating-the-value-of-ace-in-blackjack-python). ![Image of Aces Solution](https://github.com/TheS1lentArr0w/Milestone-Project-2/blob/main/Aces_Solution.png "") <br/>
(Note: This wasn't the exact solution I found but I could not find the exact Stack Overflow thread that I had at the time of coding.)

This solution was applied to the function "get_total_value" which allowed me to deal with Aces. This, however, does not give the human player a choice to decide what value their Aces will be, but this now seemed irrelevant as I got to know the game more. Basically, you treat Aces as high until they make you bust, then you treat them as low.
