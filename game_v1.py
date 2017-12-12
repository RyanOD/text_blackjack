import sys
import os
import random

os.system('clear')

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

def deal(hand):
	for x in range(0,2):
		hand.append(draw())

def draw():
	return(cards[random.randint(2,14)])

def show(player,hand,show):
	print(player,end='')
	for card in range(0,show):
		print(card)

title()

deal(hands['player'])
deal(hands['dealer'])

show('Dealer',hands['dealer'],1)
show('Player',hands['player'],2)
