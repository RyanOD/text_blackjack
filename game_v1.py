import sys
import os
import random
import math

os.system('clear')

suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
suits_symbols = ['♠', '♦', '♥', '♣']

cards = {
	2 	: 2,
	3		: 3,
	4		: 4,
	5		:	5,
	6		:	6,
	7		: 7,
	8		: 8,
	9		: 9,
	10	:	10,
	11	: "Jack",
	12	: "Queen",
	13	: "King",
	14	: "Ace"
}

hands = {
	'player' : [],
	'dealer' : []
}

def title():
	print("""
		*******************************
		*                             *
		*                             *
		*                             *
		*    Welcome to Blackjack!    *
		*                             *
		*                             *
		*                             *
		*      ♠    ♦     ♥    ♣      *
		*                             *
		*                             *
		*   Press 'enter' to begin    *
		*                             *
		*                             *
		*      ♠    ♦     ♥    ♣      *
		*                             *
		*                             *
		*                             *
		*******************************
		""")

	input()

def deal(hand):
	for x in range(0,2):
		hand.append(draw())

def draw():
	return(cards[random.randint(2,14)])

def show(hand,show):
	for card in hand:
		print(card,end=', ')

title()

deal(hands['player'])
deal(hands['dealer'])

print('Player: ',end='')
show(hands['player'],2)

# check for natural blackjack
print('\n')

print('Dealer: ',end='')
show(hands['dealer'],2)

print('\n')
