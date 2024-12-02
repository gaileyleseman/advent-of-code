from collections import Counter
from enum import Enum

class Score(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.counts = Counter(cards)

    def _calculate_combo_score(self):
        combos = list(self.counts.values())
        if 5 in combos:
            return Score.FIVE_OF_A_KIND
        if 4 in combos:
            return Score.FOUR_OF_A_KIND
        if 3 in combos and 2 in combos:
            return Score.FULL_HOUSE
        if 3 in combos:
            return Score.THREE_OF_A_KIND
        if combos.count(2) == 2:    
            return Score.TWO_PAIR
        if 2 in combos:
            return Score.PAIR
        return Score.HIGH_CARD

    def _calculate_combo_score_with_jokers(self):
        n_jokers = self.counts.pop("J", 0)
        if n_jokers == 5:  # because we pop the jokers there will be no "most common" card
            return Score.FIVE_OF_A_KIND
        most_common_card = self.counts.most_common(1)[0][0]
        self.counts[most_common_card] += n_jokers
        return self._calculate_combo_score()

    def _calculate_card_score(self, card_strength):
        return [card_strength.index(card) for card in self.cards]

    def get_combo_score(self, part=1):
        if part == 1:
            return self._calculate_combo_score().value
        s = self._calculate_combo_score_with_jokers()
        return s.value

    def get_card_scores(self, part=1):
        CARD_STRENGTH_PART_1 = "23456789TJQKA"
        CARD_STRENGTH_PART_2 = "J23456789TQKA"
        if part == 1:
            return self._calculate_card_score(CARD_STRENGTH_PART_1)
        return self._calculate_card_score(CARD_STRENGTH_PART_2)

    def __repr__(self):
        return f"Hand({self.cards}, {self.get_combo_score()}, ${self.bid})"


def parse_text(input_txt):
    data = []
    with open(input_txt, "r") as f:
        for line in f.read().split("\n"):
            cards, bid = line.split()
            data.append(Hand(cards, int(bid)))
    return data


def part1(data):
    winnings = 0
    ranked_hands = sorted(data, key=lambda x: (x.get_combo_score(), x.get_card_scores()))
    for i, hand in enumerate(ranked_hands):
        winnings += hand.bid * (i + 1)
    return winnings


def part2(data):
    winnings = 0
    ranked_hands = sorted(data, key=lambda x: (x.get_combo_score(part=2), x.get_card_scores(part=2)))
    for i, hand in enumerate(ranked_hands):
        winnings += hand.bid * (i + 1)
    return winnings

if __name__ == "__main__":
    test_data = parse_text("test.txt")
    input_data = parse_text("input.txt")

    print("TEST: Part 1: ", part1(test_data))
    print("Part 1: ", part1(input_data))

    print("TEST: Part 2: ", part2(test_data))
    print("Part 2: ", part2(input_data))
