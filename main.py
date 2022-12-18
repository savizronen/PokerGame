############### Blackjack Project #####################

import random
from art import logo
from card import Card
from cards import Cards


def deal_card(cards, suits_symbols):
    if len(cards) == 0:
        cards, suits_symbols = init_cards()

    card = random.choice(cards)
    cards.remove(card)
    suits_symbol = random.choice(suits_symbols)
    suits_symbols.remove(suits_symbol)
    return card, suits_symbol


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    cards_values = 0
    lst_cards_value = []
    for card_val in cards:
        card_num = card_val.card_number
        if card_num == 'K' or card_num == 'Q' or card_num == 'J':
            card_num = 10
        elif card_num == 1:
            card_num = 11
        lst_cards_value.append(card_num)
        cards_values += card_num

    if 11 in lst_cards_value and sum(lst_cards_value) > 21:
        for i in cards:
            if i.card_number == 11:
                i.card_number = 1
        return sum(lst_cards_value) - 10
    return sum(lst_cards_value)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def print_cards_table(game, user_score, computer_score):
    print("Your cards: ")
    print_cards(game.user_cards)
    print(f"current score: {user_score}")
    print()
    print("Computer's cards: ")
    print_cards(game.computer_cards)
    print(f"Computer's score: {computer_score}")
    print()


def play_game(cards, suits_symbols):
    print(logo)

    game = Cards()
    is_game_over = False

    for _ in range(2):
        card, suits_symbol = deal_card(cards, suits_symbols)
        game.add_user_card(card, suits_symbol)
        card, suits_symbol = deal_card(cards, suits_symbols)
        game.add_computer_card(card, suits_symbol)

    while not is_game_over:
        user_score = calculate_score(game.user_cards)
        computer_score = calculate_score(game.computer_cards)
        print_cards_table(game, user_score, computer_score)

        while (user_score < 21):
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                card, suits_symbol = deal_card(cards, suits_symbols)
                game.add_user_card(card, suits_symbol)
                user_score = calculate_score(game.user_cards)
                print_cards_table(game, user_score, computer_score)
            elif user_should_deal == "n":
                is_game_over = True
                break

        if user_score >= 21:
            is_game_over = True
        else:
            while computer_score < 17:
                card, suits_symbol = deal_card(cards, suits_symbols)
                game.add_computer_card(card, suits_symbol)
                computer_score += change_royal_to_num(card)

        print("Your final hand:")
        print_cards(game.user_cards)
        print("final score: " + str(user_score))
        print("Computer's final hand:")
        print_cards(game.computer_cards)
        print("final score: " + str(computer_score))
        print(compare(user_score, computer_score))


def init_cards():
    suits_symbols = ['♠'] * 13 + ['♦'] * 13 + ['♥'] * 13 + ['♣'] * 13
    cards = []
    for i in range(1, 11):
        card = [i] * 4
        cards.extend(card)
    royal_cards = ['J'] * 4  # King Queen Prince
    cards.extend(royal_cards)
    royal_cards = ['Q'] * 4  # King Queen Prince
    cards.extend(royal_cards)
    royal_cards = ['K'] * 4  # King Queen Prince
    cards.extend(royal_cards)
    return cards, suits_symbols


def print_cards(cards):
    cards_texture = [x.texture for x in cards]

    for i in range(0, 5):
        for card in cards_texture:
            print(card[i], end=" ")
        print()


def change_royal_to_num(card):
    if card == "K" or card == "Q" or card == "J":
        return 10
    return card


if __name__ == "__main__":
    cards, suits_symbols = init_cards()
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        play_game(cards, suits_symbols)
    print("Bye Bye")