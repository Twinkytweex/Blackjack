import random

#introduction

player_name = str(input("Please Type You're Name : "))

player = input("Hello welcome to BlackJack. press 'y' to start 'n' to end. : ").lower()




#cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#AI and Player Function

def random_card():
    Ai_player = random.choice(cards)
    return Ai_player


def add(Num1,Num2):
    return Num1 + Num2



#Main
gametrue = True

while gametrue:
    #choice
    if player == "y":
        gametrue = True

    elif player == "n":
        gametrue = False
        print("Thanks for playing")
        break
    elif player != "y" or "n":
        player = input("Type only 'y' to play or 'n' to end game. :")

    #game Engine

    # player Desk calculation
    player_card1 = random_card()
    player_card2 = random_card()
    player_total = int(add(player_card1,player_card2))
    #AI Desk calculation
    ai_card1 = random_card()
    ai_card2 = random_card()
    ai_total = int(add(ai_card1,ai_card2))
    #subtraction to not show a person AI total sum
    ai_total_hidden = ai_total - ai_card1




    #Desk
    #PLayer and AI over 21 End game
    if player_total > 21:
        print(f"{player_name} you lost [{player_card1}] [{player_card2}] Total : {player_total}. It's over 21 ")
        gametrue = False
    if ai_total > 21:
        print(f"{player_name} You won the game")

    #if player and AI not over 21.
    elif player_total <= 20:
        print(f"Dealer cards are ['HIDDEN'] [{ai_card2}] Total : {ai_total_hidden}")
        player_choice = input(f"{player_name} You're cards are [{player_card1}] [{player_card2}] Total : {player_total} You want to 'Stay' or 'Hit' : ").lower()

    #HIT choice
    while player_choice == "hit":
        if player_total > 21:
            print(f"{player_name} You have over '21' ")
            gametrue = False
            break
        elif player_total == 21:
            print(f"{player_name} You have won the game Congrats ")
            gametrue = False
            break

        #adding another card for player
        player_card3 = random_card()
        player_total = int(add(player_card3, player_total))
        if player_total > 21:
            print(f"{player_name} You have over '21' ")
            gametrue = False
            break
        Player_choice = input(f"{player_name} You're cards are [{player_card1}] [{player_card2}] [{player_card3}] Total : {player_total} You want to 'Stay' or 'Hit' : ").lower()

    #Stay Choice
    while player_choice == "stay":
        ai_card3 = random_card()
        ai_total = int(add(ai_card3,ai_total))
        if ai_total > 21:
            print(f"{player_name} You have won the game Congrats ")
            gametrue = False
            break
        elif ai_total == 21:
            print(f"{player_name} You have lost the game ")
            gametrue = False
            break
        ai_total_hidden = ai_total - ai_card1
        print(f"Dealer cards are ['HIDDEN'] [{ai_card2}] [{ai_card3}] Total : {ai_total_hidden}")
        if ai_total > player_total:
            print(f"{player_name} You have lost the game ")
            gametrue = False
            break
        elif ai_total == player_total:
            print(f"{player_name} Its a draw ")
            gametrue = False
            break
        elif ai_total <= player_total:
            print(f"{player_name} You have won the game Congrats ")
            gametrue = False
            break






