# https://www.megacolorboy.com/posts/poker-hand-analyser-in-python/
def poker_hand_ranking(hand):
    values = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    if len(set(suits)) == 1 and set(values) == {"10", "J", "Q", "K", "A"}:
        return "Royal flush"
    if len(set(suits)) == 1 and all([int(values[i]) - int(values[i - 1]) == 1 for i in range(1, 5)]):
        return "Straight flush"
    if len(set(values)) == 2 and sorted([values.count(x) for x in set(values)]) == [2, 3]:
        return "Full house"
    if len(set(suits)) == 1:
        return "Flush"
    if len(set(values)) == 5 and max([int(card[0]) for card in hand]) - min([int(card[0]) for card in hand]) == 4:
        return "Straight"
    if len(set(values)) == 3 and sorted([values.count(x) for x in set(values)]) == [1, 1, 3]:
        return "Three of a kind"
    if len(set(values)) == 4 and sorted([values.count(x) for x in set(values)]) == [1, 2, 2]:
        return "Two pair"
    if len(set(values)) == 4:
        return "One pair"
    return "High card"

