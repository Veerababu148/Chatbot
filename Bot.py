"""
This is a program for a chat bot......

1. The bot will start with a greeting nd sk for name odf the person
2  Bot will greet and welcome the person
3. Bot will ask what a person want to do it will offer a choice of thing based upon what the bot is designed for
4. It will respond to users input approximately
"""
import random
from datetime import datetime


def greeting():
    response=[
        "Hi.. My name is ChatBot. How can I help you. May I know your Name?",
        "Hello..My name is ChatBot. My I know your Name ? ",
        "Hi... This is ChatBot.I helps todo some calculations and May I know ur name"
    ]
    print(random.choice(response))


def get_timeofday_greeting():
    current_time = datetime.now()
    timeofday_greeting = "Good Morning"
    if current_time.hour > 12 and current_time.hour < 17:
        timeofday_greeting = "Good Afternoon"

    elif current_time.hour >= 17 and current_time.hour < 22:
        timeofday_greeting = "Good Evening"

    elif current_time.hour >= 22:
        timeofday_greeting = "Oh! Thats late"
    return timeofday_greeting


def welcome(name):
    messages=[
        "Nice to meet you",
        "Lets have some good time together"
    ]
    print( "Hi "+  name+" "f"{get_timeofday_greeting()}, {random.choice(messages)}")


#-----------------------------------------------------------------------------------------
def show_menu():
    print("***************************************")
    print("<----------------Select an your choice---------------->")
    print("1. Calculate an expression")
    print("2. Get current time")
    print("3. Play tick-tac-toe game")
    print("4. Guess birthday game")
    print("5. End this chat")
    print("***************************************")
    try:
        return int(input("Enter your choice [1-5] : "))
    except :
        print(" Only enter from 1,2,3,4 and 5")
        return 0
def evaluate_expression():
    expr=input("Enter an expression ")
    try:
        print("Result=",eval(expr))
    except Exception as e:
        print(str(e))


#-----------------------------------------------------------------------------------------------------------
def game():

    board = {
        'T1': ' ', 'T2': ' ', 'T3': ' ',
        'M1': ' ', 'M2': ' ', 'M3': ' ',
        'D1': ' ', 'D2': ' ', 'D3': ' '
    }

    player = 1          # to initialise first player
    total_moves = 0     # to count the moves
    end_check = 0


    def check():
        # checking the moves of player one
        # for horizontal(start)
        if board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X':
            print('Player one won !')
            return 1
        if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
            print('Player One Won!!')
            return 1
        if board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X':
            print('Player One Won!!')
            return 1
        # for horizontal(end)
        # for diagonal(start)
        if board['T1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X':
            print('Player One Won!!')
            return 1
        # for diagonal(end)
        # for vertical(start)
        if board['T1'] == 'X' and board['M1'] == 'X' and board['D1'] == 'X':
            print('Player One Won!!')
            return 1
        if board['T2'] == 'X' and board['M2'] == 'X' and board['D2'] == 'X':
            print('Player One Won!!')
            return 1
        if board['T3'] == 'X' and board['M3'] == 'X' and board['D3'] == 'X':
            print('Player One Won!!')
            return 1
        # for vertical(end)

        # checking the moves of player two
        if board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O':
            print('Player Two Won!!')
            return 1  # used to end the game
        if board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O':
            print('Player Two Won!!')
            return 1
        if board['D1'] == 'O' and board['D2'] == 'O' and board['D3'] == 'O':
            print('Player Two Won!!')
            return 1
        if board['T1'] == 'O' and board['M2'] == 'O' and board['D3'] == 'O':
            print('Player Two Won!!')
            return 1
        if board['T1'] == 'O' and board['M1'] == 'O' and board['D1'] == 'O':
            print('Player Two Won!!')
            return 1
        if board['T2'] == 'O' and board['M2'] == 'O' and board['D2'] == 'O':
            print('Player Two Won!!')
            return 1
        if board['T3'] == 'O' and board['M3'] == 'O' and board['D3'] == 'O':
            print('Player Two Won!!')
            return 1
        return 0


    print('T1|T2|T3')
    print('- +- +-')
    print('M1|M2|M3')
    print('- +- +-')
    print('D1|D2|D3')
    print('***************************')

    while True:
        print(board['T1']+'|'+board['T2']+'|'+board['T3'])
        print('-+-+-')
        print(board['M1'] + '|' + board['M2'] + '|' + board['M3'])
        print('-+-+-')
        print(board['D1'] + '|' + board['D2'] + '|' + board['D3'])
        end_check = check()
        if total_moves == 9 or end_check == 1:
            break
        while True:     # input from players
            if player == 1:  # choose player
                p1_input = input('player one : ')
                if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                    board[p1_input.upper()] = 'X'
                    player = 2
                    break
                # on wrong input
                else:
                    print('Invalid input, please try again')
                    continue
            else:
                p2_input = input('player two : ')
                if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                    board[p2_input.upper()] = 'O'
                    player = 1
                    break
                else:  # on wrong input
                    print('Invalid input, please try again')
                    continue
        total_moves += 1
        print('***************************')
        print()

#--------------------------------------------------------------------------------------------------------------------

def guess_number():
    a=int(input("Enter birth day :"))
    b=int(input("Enter month date :"))
    m=(((a*2)+5)*50)+b-250

    k=m%100
    l=m//100
    print("date/month is :",l,"/",k,sep="")


def bot():
    greeting()
    name=input("Enter your name please : ")
    welcome(name)
    choice=show_menu()
    while choice !=5:
        if choice==1:
            evaluate_expression()
        elif choice==2:
            print(str(datetime.now()))
        elif choice==3:
            game()
        elif choice==4:
            guess_number()
        else:
            print("I dont understand that")
        choice=show_menu()


bot()



