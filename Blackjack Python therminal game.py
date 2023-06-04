import random

# deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(rank, suit) for suit in suits for rank in ranks]

# calculate the total value of a hand
def calculate_hand_value(hand):
    values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
    value = sum(values[card[0]] for card in hand)
    # Adjust for Aces
    for card in hand:
        if card[0] == 'Ace' and value > 21:
            value -= 10
    return value

# deal a card from the deck
def deal_card():
    return deck.pop()

# play the game
def play_game():
    player_hand = []
    dealer_hand = []

    # Deal initial cards
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())

    # Game loop
    while True:
        print("Player's hand:", player_hand)
        print("Dealer's hand:", dealer_hand[0])

        # Check if player or dealer has blackjack
        if calculate_hand_value(player_hand) == 21:
            print("Player wins with a blackjack!")
            break
        elif calculate_hand_value(dealer_hand) == 21:
            print("Dealer wins with a blackjack!")
            break

        # Ask player to hit or stand
        choice = input("Do you want to hit or stand? ")
        if choice.lower() == 'hit':
            player_hand.append(deal_card())
            if calculate_hand_value(player_hand) > 21:
                print("Player busts! Dealer wins.")
                break
        elif choice.lower() == 'stand':
            # Dealer's turn
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deal_card())
            print("Dealer's hand:", dealer_hand)

            player_value = calculate_hand_value(player_hand)
            dealer_value = calculate_hand_value(dealer_hand)

            if dealer_value > 21:
                print("Dealer busts! Player wins.")
            elif player_value > dealer_value:
                print("Player wins!")
            elif dealer_value > player_value:
                print("Dealer wins!")
            else:
                print("It's a tie!")
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")

# Main function
def main():
    print("Welcome to Blackjack!")
    play_game()

# Run the main function
if __name__ == '__main__':
    main()
