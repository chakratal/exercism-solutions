"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

cards_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

card_in_hand = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of given card (see values below).

    1.  'J', 'Q', or 'K' (a.k.a. - "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    return cards_dict.get(card)

def higher_card(card_one, card_two):
    """Determine which card in the hand has a higher value.

    :param card_one, card_two: str - cards dealt in hand (see below for values).
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (a.k.a. - "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if cards_dict.get(card_one) > cards_dict.get(card_two):
        return card_one
    if cards_dict.get(card_two) > cards_dict.get(card_one):
        return card_two
    return (card_one, card_two)

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (a.k.a. - "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
         
    if card_in_hand.get(card_one) + card_in_hand.get(card_two) > 10:
        return 1
    return 11

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt (see values below).
    :return: bool - the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (a.k.a. - "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    blackjack = (card_in_hand.get(card_one) == 11 or card_in_hand.get(card_two) == 11) and (card_in_hand.get(card_one) == 10 or card_in_hand.get(card_two) == 10)

    return blackjack

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs (cards are of the same value)?
    """

    return cards_dict.get(card_one) == cards_dict.get(card_two)

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down (totaling 9, 10 or 11 points)?
    """
    nine = cards_dict.get(card_one) + cards_dict.get(card_two) == 9
    ten = cards_dict.get(card_one) + cards_dict.get(card_two) == 10
    eleven = cards_dict.get(card_one) + cards_dict.get(card_two) == 11

    return nine or ten or eleven
