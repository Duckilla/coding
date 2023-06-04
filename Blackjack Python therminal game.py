import random

# deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        if self.value > 21 and 'Ace' in [card.rank for card in self.cards]:
            self.value -= 10

# hitting or standing
def hit_or_stand():
    while True:
        choice = input("Do you want to hit or stand? Enter 'h' or 's': ")
        if choice.lower() == 'h':
            return 'hit'
        elif choice.lower() == 's':
            return 'stand'
        else:
            print("Invalid input. Please enter 'h' or 's'.")

# display player's and dealer's hands
def show_hands(player_hand, dealer_hand, show_all_cards=False):
    print("\nPlayer's Hand:")
    for card in player_hand.cards:
        print(card)
    print("Total value:", player_hand.value)

    if show_all_cards:
        print("\nDealer's Hand:")
        for card in dealer_hand.cards:
            print(card)
        print("Total value:", dealer_hand.value)
    else:
        print("\nDealer's Hand:")
        print(dealer_hand.cards[0])
        print("Total value: ???")

def play_game():
    print("Welcome to Blackjack!\n")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    show_hands(player_hand, dealer_hand)

    # Continue playing until player stands or goes bust
    while True:
        choice = hit_or_stand()
        if choice == 'hit':
            player_hand.add_card(deck.deal_card())
        show_hands(player_hand, dealer_hand)
        
        # Check if player goes bust (value exceeds 21)
        if player_hand.value > 21:
            print("You went bust! Dealer wins.")
            break
        
        # Player stands, now it's the dealer's turn
        if choice == 'stand':
            # Show the dealer's hidden card
            show_hands(player_hand, dealer_hand, show_all_cards=True)
            
            # Dealer hits until their hand value reaches 17 or more
            while dealer_hand.value < 17:
                dealer_hand.add_card(deck.deal_card())
            
            # Show the final hands of both player and dealer
            show_hands(player_hand, dealer_hand, show_all_cards=True)
            
            # Determine the winner
            if dealer_hand.value > 21:
                print("Dealer went bust! You win.")
            elif dealer_hand.value > player_hand.value:
                print("Dealer wins.")
            elif dealer_hand.value < player_hand.value:
                print("You win!")
            else:
                print("It's a tie!")
            
            break

# Start the game
play_game()
