import sys
import os
import random
import math

os.system('clear')

ranks = [_ for _ in range(2,11)] + ['Jack', 'Queen', 'King', 'Ace']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
suits_symbols = {'Clubs' : '♣', 'Diamonds' : '♦', 'Hearts' : '♥', 'Spades' : '♠'}

def get_deck():
	return [[rank, suit] for rank in ranks for suit in suits]

def deal_card(deck):
	return deck.pop()

deck = get_deck()
random.shuffle(deck)

player_hand = [deal_card(deck), deal_card(deck)]
dealer_hand = [deal_card(deck), deal_card(deck)]

print(player_hand)
