from random import randrange
__all__ = ['create_deck', 'shuffle', 'compare_cards']

# A global dict to get the rank's value and also to check if the rank is valid
VALUE_OF_RANK = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                 '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# A global list of suites to check if some suite is valid
SUITES_LIST = ['H', 'C', 'D', 'S']


def create_card(rank: str, suite: str) -> dict:
    if rank not in VALUE_OF_RANK:
        raise Exception("Invalid rank!!!")
    if suite not in SUITES_LIST:
        raise Exception("Invalid suite!!!")
    return {"rank": rank, "suite": suite, "value": VALUE_OF_RANK[rank]}


def is_valid_card(card: dict) -> bool:
    if len(card) != 3:
        return False
    if card.get("rank", 0) not in VALUE_OF_RANK:
        return False
    if card.get("suite", 0) not in SUITES_LIST:
        return False
    if card.get("value", 0) != VALUE_OF_RANK[card["rank"]]:
        return False
    else:
        return True


def is_valid_deck(deck: list[dict]) -> bool:
    return len(deck) == 52 and all(map(is_valid_card, deck))


def compare_cards(p1_card: dict, p2_card: dict) -> str:
    if not is_valid_card(p1_card):
        raise Exception("Invalid player 1 card!!!")
    if not is_valid_card(p2_card):
        raise Exception("Invalid player 2 card!!!")
    if p1_card["value"] > p2_card["value"]:
        return 'p1'
    elif p1_card["value"] < p2_card["value"]:
        return 'p2'
    else:
        return 'WAR'


def create_deck() -> list[dict]:
    deck = list()
    for suite in SUITES_LIST:
        for rank in VALUE_OF_RANK:
            deck.append(create_card(rank, suite))
    return deck


def shuffle(deck: list[dict]) -> list[dict]:
    if not is_valid_deck(deck):
        raise Exception("Invalid deck!!!")
    for i in range(1000):
        index1 = 0
        index2 = 0
        while index1 == index2:
            index1 = randrange(52)
            index2 = randrange(52)
        deck[index1], deck[index2] = deck[index2], deck[index1]
    return deck
