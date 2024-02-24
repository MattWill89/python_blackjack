import random

def main():
    """Main game loop."""
    def deal_card():
        """Returns a random card from the deck."""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def calculate_score(hand):
        """Calculates the score of a hand, treating Aces as 1 or 11."""
        score = sum(hand)
        if 11 in hand and score > 21:
            score -= 10
        return score

    def play_again():
        """Asks the player if they want to play again."""
        while True:
            choice = input("Would you like to play again? (y/n): ").lower()
            if choice in ["y", "n"]:
                return choice == "y"
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    print("Welcome to Blackjack!")

    while True:
        # Ask if the player wants to play
        play = input("Do you want to play Blackjack? (y/n): ").lower()
        if play != "y":
            break

        # Deal initial cards
        player_hand = [deal_card(), deal_card()]
        dealer_hand = [deal_card(), deal_card()]

        # Player's turn
        while True:
            print("Your hand:", player_hand)
            print("Dealer's hand:", dealer_hand[0], "??" )  # Hide dealer's second card

            if calculate_score(player_hand) > 21:
                print("You busted! Dealer wins.")
                break

            choice = input("Hit or stand? (h/s): ").lower()
            if choice == "s":
                break
            elif choice == "h":
                player_hand.append(deal_card())
            else:
                print("Invalid input. Please enter 'h' or 's'.")

        # Dealer's turn
        if calculate_score(player_hand) <= 21:
            print("\nDealer's turn")
            while calculate_score(dealer_hand) < 17:
                dealer_hand.append(deal_card())
            print("Dealer's hand:", dealer_hand)

            player_score = calculate_score(player_hand)
            dealer_score = calculate_score(dealer_hand)

            if dealer_score > 21:
                print("Dealer busts! You win!")
            elif dealer_score > player_score:
                print("Dealer wins!")
            elif dealer_score < player_score:
                print("You win!")
            else:
                print("It's a tie!")

        # Ask if the player wants to play again
        if not play_again():
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
