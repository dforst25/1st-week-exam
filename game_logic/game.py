from utils.deck import *

__all__ = ['init_game', 'play_round', 'count_hearts']


def create_player(name: str = 'AI') -> dict:
    return {"name": name, "hand": [], "won_pile": []}


def init_game() -> dict:
    p1 = create_player("David")
    p2 = create_player()
    deck = create_deck()
    deck = shuffle(deck)
    p1["hand"] = deck[:26]
    p2["hand"] = deck[26:]
    return {'deck': deck, 'player_1': p1, 'player_2': p2}


def print_player(player_name: str) -> None:
    print(f'{player_name} took this round!!!')


def print_cards(card_list: list[dict]) -> None:
    print("the cards are:")
    for i in range(len(card_list)):
        print(f'''\t{i + 1}) {card_list[i]['suite']} - {card_list[i]['rank']}''')


def play_round(p1: dict, p2: dict) -> None:
    p1_card = p1['hand'].pop(0)
    p2_card = p2['hand'].pop(0)
    winner = compare_cards(p1_card, p2_card)
    if winner == 'p1':
        p1['won_pile'].extend([p1_card, p2_card])
        print_player(p1['name'])
    elif winner == 'p2':
        p2['won_pile'].extend([p1_card, p2_card])
        print_player(p2['name'])
    else:
        print(winner)
        play_war(p1, p2, [p1_card, p2_card])
        return
    print_cards([p1_card, p2_card])


def play_war(p1: dict, p2: dict, card_list: list[dict]) -> None:
    if len(p1['hand']) > 3 and len(p2['hand']) > 3:
        min_len = 4
    else:
        min_len = min(len(p1['hand']), len(p2['hand']))
        if min_len == 0:
            return
    card_list.extend(p1['hand'][:min_len] + p2['hand'][:min_len])
    p1_card3 = p1['hand'][min_len - 1]
    p2_card3 = p2['hand'][min_len - 1]
    p1['hand'] = p1['hand'][min_len:]
    p2['hand'] = p2['hand'][min_len:]
    winner = compare_cards(p1_card3, p2_card3)
    if winner == 'p1':
        p1['won_pile'].extend(card_list)
        print_player(p1['name'], )
    elif winner == 'p2':
        p2['won_pile'].extend(card_list)
        print_player(p2['name'])
    else:
        print(winner)
        play_war(p1, p2, [p1_card3, p2_card3])
    print_cards(card_list)


def count_hearts(player: dict) -> int:
    return len(list(filter(lambda card: card['suite'] == 'H', player['won_pile'])))
