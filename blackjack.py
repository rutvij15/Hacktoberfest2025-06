import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def value(self):
        if self.rank in ['J','Q','K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(s,r) for s in suits for r in ranks]
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def value(self):
        val = sum(card.value() for card in self.cards)
        # Adjust for aces
        aces = sum(1 for card in self.cards if card.rank == 'A')
        while val > 21 and aces:
            val -= 10
            aces -= 1
        return val
    
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

def play_blackjack():
    deck = Deck()
    player = Hand()
    dealer = Hand()

    # Initial draw
    for _ in range(2):
        player.add_card(deck.draw())
        dealer.add_card(deck.draw())
    
    while True:
        print(f"\nYour hand ({player.value()}): {player}")
        print(f"Dealer shows: {dealer.cards[0]}")
        
        if player.value() == 21:
            print("Blackjack! You win!")
            return
        if player.value() > 21:
            print("Bust! You lose.")
            return
        
        move = input("Hit or Stand? (h/s): ").lower()
        if move == 'h':
            player.add_card(deck.draw())
        elif move == 's':
            break
        else:
            print("Invalid input.")

    # Dealer turn
    print(f"\nDealer's hand ({dealer.value()}): {dealer}")
    while dealer.value() < 17:
        dealer.add_card(deck.draw())
        print(f"Dealer draws: {dealer.cards[-1]} (Total: {dealer.value()})")
    
    if dealer.value() > 21 or player.value() > dealer.value():
        print("You win!")
    elif player.value() == dealer.value():
        print("Draw!")
    else:
        print("Dealer wins!")

if __name__ == "__main__":
    while True:
        play_blackjack()
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            break
