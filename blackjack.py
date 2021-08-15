'''
BlackJack Card Game
'''

# Imports
import random

# Global variables that will be useful throughout the code

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

### Creation of required objects

# Creation of Card class
class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Creation of Deck class
class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create each card object and add it to the deck
                created_card = Card(suit,rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)
        print("The deck has been shuffled!")

    def deal_one(self):
        return self.all_cards.pop()

# Creation of Player class
class Player:
    
    def __init__(self,bankroll):
        self.all_cards = []
        self.bankroll = bankroll
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # list of multiple Card objects
            # PROBABLY WON'T NEED THIS CASE BUT HANDY FOR NOW
            self.all_cards.extend(new_cards)
        else:
            # for a single Card object
            self.all_cards.append(new_cards)

# Creation of Dealer class
class Dealer(Player):

    def __init__(self):
        self.all_cards = []

    # Due to inheritance, Dealer will also have 'remove_one' and 'add_cards' methods.
    # Redefining __init__ call as Dealer does not require a bankroll.

### Creation of required functions

# Player input for bet
# Check for errors e.g. has to be int, minimum 100, cannot exceed bankroll
def player_bet(bankroll):

    choice = "WRONG"
    greater_than_min = False
    not_exceeding = False

    while choice.isdigit()==False or greater_than_min==False or not_exceeding==False:

        choice = input("How much will you bet? (Minimum bet = 100): ")

        # Digit check
        if choice.isdigit() == False:
            print("Sorry, that is not a digit!")

        # Greater than 100 check
        if choice.isdigit() == True:
            if int(choice) > 100:
                greater_than_min = True
            else:
                print("Sorry! The minimum bet is 100!")
                greater_than_min = False

        # Not exceeding bankroll check
        if choice.isdigit() == True:
            if greater_than_min == True:
                if int(choice )< bankroll:
                    not_exceeding = True
                else:
                    print("Sorry, that bet is more than what you have!")
                    not_exceeding = False

    return int(choice)

# Player input for hit or stay
def player_choice():

    choice = "WRONG"
    acceptable_values = ["hit","stay"]

    while choice not in acceptable_values:

        choice = input("Do you choose to hit or stay? (Please enter 'hit' or 'stay'): ")

        if choice not in acceptable_values:
            print("Sorry, I do not understand. Please enter 'hit' or 'stay'.")

    return choice

# Player input for playing again
def play_again():

    choice = "WRONG"
    acceptable_values = ['y','n']

    while choice not in acceptable_values:

        choice = input("Do you want to play again? ('y' or 'n'): ")

        if choice not in acceptable_values:
            print("Sorry, I do not understand. Please enter 'y' or 'n'.")

    return choice

# Getting total value
def get_total_value(all_cards):
    total_value = 0
    aces = 0

    for card in all_cards:
        total_value += card.value

        if card.rank == 'Ace':
            aces += 1

    while aces > 0 and total_value > 21:
        total_value -= 10
        aces -= 1

    return total_value

##### MAIN GAME LOGIC

playing = True

### Initiate game

print("Welcome to Blackjack!")

new_deck = Deck()
# Shuffle deck
new_deck.shuffle()

# Player initiate
new_player = Player(1000)

# Dealer initiate
new_dealer = Dealer()

### Main game loop

while playing:

    # Display bankroll
    print(f"Your current bankroll is: {new_player.bankroll}")

    # Check if Player is broke
    if new_player.bankroll < 100:
        print("Sorry, you do not have enough money to play!")
        playing = False
        break

    # Ask for bet
    bet = player_bet(new_player.bankroll)

    # Deal cards, one each twice.
    for i in [1,2]:
        new_player.all_cards.append(new_deck.deal_one())
        new_dealer.all_cards.append(new_deck.deal_one())
    print("The cards have been dealt!")

    # Show 1 card from the dealer
    print("Dealer cards:")
    print(new_dealer.all_cards[0])
    print("UNKNOWN")

    # Show both cards from the player
    print("Player cards:")
    for card in new_player.all_cards:
        print(card)

    # Loop for Player's turn
    bust = False

    while bust == False:

        # Ask for player choice
        choice = player_choice()

        if choice == "hit":
            new_player.all_cards.append(new_deck.deal_one())
        else:
            # if player chose 'stay'
            break


        # Display cards again
        print("Player cards:")
        for card in new_player.all_cards:
            print(card)

        # Check for bust
        total_value = get_total_value(new_player.all_cards)
        
        if total_value > 21:
            print("Bust!")
            bust = True
            break


    # Loop for Dealer's turn
    dealer_bust = False
    while dealer_bust == False:
        # if total_value >= 17, stay. Else, hit.
        total_value = get_total_value(new_dealer.all_cards)

        if total_value < 17:
            # hit
            new_dealer.all_cards.append(new_deck.deal_one())
        elif total_value >= 17 and total_value <= 21:
            # stay
            break
        else:
            # bust
            print("Dealer has bust!")
            dealer_bust = True
            break

    # Reveal cards
    print("The player and the dealer have ended their turn.")

    # Dealer cards
    print("Dealer cards:")
    for card in new_dealer.all_cards:
        print(card)
    print(f"The value of the dealer's hand = {get_total_value(new_dealer.all_cards)}")

    # Player cards
    print("Player cards:")
    for card in new_player.all_cards:
        print(card)
    print(f"The value of the player's hand = {get_total_value(new_player.all_cards)}")


    ### Checking game outcomes

    # Checking if player bust
    if bust == True:
        # Player bust
        # Player lose, subtract 2xbet from player bankroll
        new_player.bankroll -= 2*bet

    # Checking if dealer bust
    if bust == False and dealer_bust == True:
        # Dealer bust but player doesn't bust
        # Player win
        new_player.bankroll += 2*bet

    # Neither bust. Compare total_values
    player_total = get_total_value(new_player.all_cards)
    dealer_total = get_total_value(new_dealer.all_cards)

    if player_total > dealer_total:
        # Player win
        new_player.bankroll += 2*bet
    elif player_total < dealer_total:
        # Player lose
        new_player.bankroll -= 2*bet
    else:
        # Tie
        # No money lost or gained
        pass

    # Updated bankroll
    print(f"Your updated bankroll is: {new_player.bankroll}")

    # Play again?
    choice = play_again()
    if choice == 'y':
        pass
    else:
        playing = False
        break