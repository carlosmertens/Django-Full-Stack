#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Variable representing the Suits (Hearts, Diamonds, Spades and Clubs)
suits = 'H D S C'.split()

# Variable representing Ranks (2 to 10 and Js, Qs, Ks and As)
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        """Initiate by creating a deck of cards."""
        print("Creating new ordered deck of cards...")
        self.all_cards = [(s, r) for s in suits for r in ranks]
        # print(self.all_cards)

    def shuffle(self):
        """Shuffle newly created deck."""
        print("Shuffling the deck...")
        shuffle(self.all_cards)
        # print(self.all_cards)

    def split_deck(self):
        """Split shuffled deck in 2 halves."""
        print("Splitting the shuffled deck...\n")
        # Remove "print" below after debugging
        return (self.all_cards[:26], self.all_cards[26:])


class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self, cards):
        """Initiate cards at hand."""
        self.cards = cards

    def __str__(self):
        """Return String Presentation of players cards at hand."""
        return "** Contains {} cards!".format(len(self.cards))

    def add_cards(self, added_cards):
        """Add card(s) on the table's game."""
        self.cards.extend(added_cards)

    def remove_cards(self):
        """Remove card(s) from the table's game"""
        return self.cards.pop()


class Player():
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand):
        """Initate players."""
        self.name = name
        self.hand = hand

    def play_card(self):
        """Call card from players' deck to the table's game."""
        drawn_card = self.hand.remove_cards()
        print("{} has played: {}".format(self.name, drawn_card))
        return drawn_card

    def remove_war_cards(self):
        """Remove 3 cards from players' deck on WAR rounds."""
        war_cards = []
        # Check if players have enough cards for WAR round
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for i in range(3):
                war_cards.append(self.hand.remove_cards())
            return war_cards

    def still_has_cards(self):
        """Check if there is still cards in player' deck."""

        return len(self.hand.cards) != 0


######################
#### GAME PLAY #######
######################

print("\n\t\tWELCOME TO WAR!!!\nLet's begin...\n")

# Create new deck, shuffle it and split it in half
game_deck = Deck()
game_deck.shuffle()
half1, half2 = game_deck.split_deck()

# Create players
computer = Player("Computer", Hand(half1))
player_name = input("Your name: ")
user = Player(player_name, Hand(half2))

# Create logic of the game
total_rounds = 0
war_count = 0

while user.still_has_cards() and computer.still_has_cards():
    total_rounds += 1
    print("** CURRENT STANDING:")
    print(user.name + " has the count: " + str(len(user.hand.cards)))
    print(computer.name + " has the count: " + str(len(computer.hand.cards)))
    print("** PLAY CARDS")

    # Play players (computer and user)
    table_cards = []

    comp_card = computer.play_card()
    user_card = user.play_card()

    table_cards.append(comp_card)
    table_cards.append(user_card)

    # Check for WAR
    if comp_card[1] == user_card[1]:  # Index 1 to compare their Ranks
        war_count += 1
        print("WAR!!!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(computer.remove_war_cards())

        # Check for WAR hand winner
        if ranks.index(comp_card[1]) < ranks.index(user_card[1]):
            user.hand.add_cards(table_cards)
        else:
            computer.hand.add_cards(table_cards)
    else:
        # Check for normal hand winner
        if ranks.index(comp_card[1]) < ranks.index(user_card[1]):
            user.hand.add_cards(table_cards)
        else:
            computer.hand.add_cards(table_cards)

# Game Over
print("We have a winner!!!")
print("Round played: " + str(total_rounds))
print("War played: " + str(war_count))

# Reporting the winner
if user.still_has_cards():
    print("Congratulations, {}. You are a champion!".format(user.name))
else:
    print("Sorry, {}. You lost!".format(user.name))
