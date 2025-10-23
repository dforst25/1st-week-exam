from game_logic.game import *

if __name__ == "__main__":
    game = init_game()
    p1 = game['player_1']
    p2 = game['player_2']
    deck = game['deck']
    while len(p1['hand']) and len(p2['hand']):
        play_round(p1, p2)
    if len(p1['won_pile']) > len(p2['won_pile']):
        print(f"{p1['name']} won!!!")
    elif len(p1['won_pile']) < len(p2['won_pile']):
        print(f"{p2['name']} won!!!")
    elif count_hearts(p1) > count_hearts(p2):
        print(f"{p1['name']} won!!!\nbecause he has more hearts ({p1['name']} has {count_hearts(p1)} hearts and {p2['name']} has {count_hearts(p2)} hearts.)")
    else:
        print(f"{p2['name']} won!!!\nbecause he has more hearts ({p2['name']} has {count_hearts(p2)} hearts and {p1['name']} has {count_hearts(p1)} hearts.)")
