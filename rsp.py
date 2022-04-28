#!/usr/bin/env python3
import time

import random


moves = ['rock', 'paper', 'scissors']

cycle = 0

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

# validate user input


def valid_input(prompt):
    while True:
        response = input(prompt).lower()
        if response in moves:
            return response
        else:
            print_pause("Sorry, this is invalid. Try again!")


def game_intro():
    print_pause("*** Welcome to Rock, Paper, Scissors Game! ***\n")
    print_pause("This program plays a game of Rock, Paper, Scissors!\n")
    print_pause("Between two Players! \n")
    print_pause("And reports both Player's scores each round. \n")
    print_pause("You can play as many Rounds as you want!\n")
    print_pause("Let's Go!!!")


# create a parent class called Player

class Player:
    moves = ['rock', 'paper', 'scissors']
    move1 = random.choice(moves)
    move2 = random.choice(moves)
    score = 0
    my_own_move = " "
    opp_move = " "

    def move(self):
        return 'rock'

    def learn(self, my_own_move, opp_move):
        self.opp_move = opp_move
        self.my_own_move = my_own_move
        self.my_next_move = opp_move


# create 4 Inheritances called RockPlayer,HumanPlayer,RandomPlayer &CyclePlayer

# creating a class that always plays rock.
class RockPlayer(Player):
    def move(self):
        return "rock"

# subclass RandomPlayer chooses its move at random.


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)

# HumanPlayer Subclass ask the human user what move to make


class HumanPlayer(Player):

    def move(self):
        response = valid_input("Enter rock, paper or scissors \n")
        return response

# creating a class that remembers the last move the opponent made


class ReflectPlayer(Player):
    def __init__(self):
        self.my_next_move = random.choice(moves)

    def move(self):
        return self.my_next_move

    def learn(self, my_own_move, opp_move):
        self.my_next_move = opp_move


"""calling the learn method on each player"""


class CyclePlayer(Player):
    def __init__(self):
        self.my_own_move = random.choice(moves)

    def move(self):
        if self.my_own_move == "rock":
            return "scissors"
        if self.my_own_move == "scissors":
            return "paper"
        if self.my_own_move == "paper":
            return "rock"

    def learn(self, my_own_move, opp_move):
        self.my_own_move = my_own_move
        self.opp_move = opp_move
        self.my_next_move = opp_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


"""create the starter class Game
The Game class will have the play_game,
play_again and play_round, winner functions
Player1 & player2 are object.Object is an instance of the class game."""


class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.round = []
        self.p1_score = 0
        self.p2_score = 0
        # self.moves = ["rock", "paper", "scissors"]

    # HumanPlayer = Player()

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"Player 1: {move1} vs Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        # calling the beats funtion beats()
        if beats(move2, move1) is True:
            print_pause("**** Winner of this round is Player 2 **** \n ")
            self.p2_score = 1
        elif beats(move1, move2) is True:
            print_pause("**** Winner of this round is Player 1 **** \n ")
            self.p1_score = 1
        elif move1 == move2:
            print_pause("**** It is a Draw!**** \n ")
        print_pause(f"You played {move1}")
        print_pause(f"Player two played {move2}")
        print_pause(f"Points: {self.p1_score} , {self.p2_score} \n")

    def play_again(self):
        while True:
            response = input("\n Would you like to Play again? "
                             "Enter yes or no \n")
            if response == "no":
                print_pause("Goodbye! See you soon!")
                exit()
            elif response == "yes":
                print_pause("Excellent! Starting Game!")
                game.play_game()
            else:
                print_pause("Invalid Input! Try again!")
                self.play_again()

    def play_game(self):
        print_pause("Game start!")
        self.round = input("How many rounds do you want to play? \n")
        while True:
            if self.round.isnumeric():
                print_pause(f"Great! your best {self.round} rounds!")
                self.round = int(self.round)
                break
            else:
                print_pause("Please enter a positive number greater than 0 \n")
                self.round = input("How many rounds do you want to play? \n")
        for round in range(self.round):
            print_pause(f"Round {round}:")
            self.play_round()
            print_pause(f"Player 1 score is {self.p1_score} point.\n")
            print_pause(f"Player 2 score is {self.p2_score} point.\n")
            self.Scoreboard()
            print_pause("Round over!")
        self.Scoreboard()
        self.play_again()

    def Scoreboard(self):
        # if round == 5:

        if self.p1_score > self.p2_score:
            print_pause("**** The winner is Player 1! **** \n")
            self.p1_score += 1
        elif self.p2_score > self.p2_score:
            print(" **** The winner is player 2! **** \n")
            self.p2_score += 1
        elif self.p1_score == self.p2_score:
            print(" **** It is a Draw! ***** \n")

# calling players to randomly play against each other

if __name__ == '__main__':
    game_intro()
    strategy = {"1": RockPlayer(), "2": RandomPlayer(),
                "3": CyclePlayer(), "4": ReflectPlayer()}
    user_input = ""
    while user_input not in strategy:
        user_input = input("Which Player do You want to play against? \n "
                           "Type: 1, 2, 3, or 4 \n"
                           "1- RockPlayer \n"
                           "2- CyclePlayer \n"
                           "3- RandomPlayer \n"
                           "4- ReflectPlayer \n")

    game = Game(HumanPlayer(), strategy[user_input])
    game.play_game()
