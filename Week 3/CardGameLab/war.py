"""Game of War

Code by Josh Blumberg
Based on rules from: https://gamerules.com/rules/war-card-game/
"""
from cards import Card, Deck, Player
from time import sleep
from random import shuffle

# Game Setup
players = [Player(input(f'What is the name of player {n}: ')) for n in range(1, 3)]
war_pile = []
game_speed = 0  # Number of seconds to pause between rounds
PLAYER_1 = 0
PLAYER_2 = 1

# Deal all of the cards
deck = Deck()
deck.shuffle()
while True:
    try:
        players[PLAYER_1].add_cards_to_bottom([deck.draw_card()])
        players[PLAYER_2].add_cards_to_bottom([deck.draw_card()])
    except IndexError:
        break


# Main game loop
while players[PLAYER_1].cards and players[PLAYER_2].cards:  # While both players have cards
    print('-'*20)
    sleep(game_speed)
    drawn_cards = [player.draw_from_top() for player in players]
    for n, card in enumerate(drawn_cards):
        print(f'{players[n].name} plays the {card}')

    if drawn_cards[PLAYER_1].value() != drawn_cards[PLAYER_2].value():  # If there is a clear winner
        if drawn_cards[PLAYER_1].value() > drawn_cards[PLAYER_2].value():
            winner = PLAYER_1
        else:
            winner = PLAYER_2

        print(f'{players[winner].name} Won!')
        print(f'{players[winner].name} is adding the following cards to their deck:')
        for card in drawn_cards + war_pile:
            print(card)
        won_cards = drawn_cards + war_pile
        shuffle(won_cards)
        players[winner].add_cards_to_bottom(won_cards)
        war_pile = []

    else:  # We have a War (tie situation)
        print(f'Adding 3 cards from each player to the War Pile')
        war_pile.extend(drawn_cards)
        try:
            war_pile.extend([players[PLAYER_1].draw_from_top() for n in range(3)])
        except IndexError:
            print(f'{players[PLAYER_1].name} ran out of cards')
            break
        try:
            war_pile.extend([players[PLAYER_2].draw_from_top() for n in range(3)])
        except IndexError:
            print(f'{players[PLAYER_2].name} ran out of cards')
            break

        print(f'3.. 2.. 1.. War!')

print('-------- Game Over --------')
if players[PLAYER_1].cards:  # If player 1 still has cards
    print(f'{players[PLAYER_1].name} won the game!')
else:
    print(f'{players[PLAYER_2].name} won the game!')
