import math
import re

total_points = 0
with open("data/Day4_1.txt", "r") as data:
    cards = data.readlines()
    cards = cards.split("\n")

for card in cards:

    # preprocessing of the text values, split strings into original card and your card
    card = card.split(":")[-1].split("|")
    card = [s.strip() for s in card]

    # identify numbers in the original card, and in your card
    card_number = re.findall("\d+", card[0])
    your_card = re.findall("\d+", card[1])

    # get count of matches between the cards
    n = len([_ for _ in your_card if _ in card_number])

    # accumulate total points
    total_points += math.floor(2 ** (n - 1))
