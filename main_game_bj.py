#!/usr/bin/env python
from random import randint
import time

def cr():
    temp = randint(1,4)
    return temp
def nr():
    temp = randint(1,13)
    return temp

account_total = 1000
cards_in_game = []
player_cards = []
player_cards_1 = []
player_bet = 0
player_bet_1 = 0
player_card_value = 0
player_card_value_1 = 0

class Card():
    cards = []
    def __init__(self, color, number) -> None:
        self.color = color
        self.number = number
    
    def create_card(self):
        temp_color = ''
        temp_number = ''
        temp_value = 0
        if self.color == 1:
            temp_color = 'hearts'
        elif self.color == 2:
            temp_color = 'cloves'
        elif self.color == 3:
            temp_color = 'diamonds'
        else:
            temp_color = 'spades'
        
        if self.number == 1:
            temp_number = "ace"
            temp_value = 11
        elif self.number == 2:
            temp_number = "two"
            temp_value = 2
        elif self.number == 3:
            temp_number = "three"
            temp_value = 3
        elif self.number == 4:
            temp_number = "four"
            temp_value = 4
        elif self.number == 5:
            temp_number = "five"
            temp_value = 5
        elif self.number == 6:
            temp_number = "six"
            temp_value = 6
        elif self.number == 7:
            temp_number = "seven"
            temp_value = 7
        elif self.number == 8:
            temp_number = "eight"
            temp_value = 8
        elif self.number == 9:
            temp_number = "nine"
            temp_value = 9
        elif self.number == 10:
            temp_number = "ten" 
            temp_value = 10
        elif self.number == 11:
            temp_number = "jack"
            temp_value = 10
        elif self.number == 12:
            temp_number = "queen"
            temp_value = 10
        elif self.number == 13:
            temp_number = "king"  
            temp_value = 10
        self.cards.append([temp_color, temp_number, temp_value])

def correct_name():
    name_correct = False
    while name_correct == False:
        name = input("Please tell us your name:\n")
        if len(name) < 20:
            name_correct = True
        else:
            print("Maximum characters is 20.")
    return name

print("\nHi, and welcome to the blackjack game!\n     ♠ ♥ ♦ ♣ ")                  
name = correct_name()
print("Good to see you " + name + "!")

def main():      
    global account_total, player_bet,player_bet_1,player_card_value,player_card_value_1,player_cards, player_cards_1, name
    if account_total <= 0:
        print("No more funds. See you next time!")
        exit()
    Card.cards = []
    player_cards = []
    player_cards_1 = []
    player_bet = 0
    player_bet_1 = 0
    player_card_value = 0
    player_card_value_1 = 0
    def new_game():
        new_card_1 = Card(randint(1,4), randint(1,13))
        new_card_1.create_card()

        new_card_2 = Card(randint(1,4), randint(1,13))
        new_card_2.create_card()

        player_cards.extend(new_card_1.cards)
        cards_in_game.extend(new_card_1.cards)

    def correct_bet():
        global account_total
        bet_correct = False
        while bet_correct == False:
            try:
                bet = int(input())
            except:
                print("Please enter a number")
            else:
                if bet > account_total:
                    print("Not enough funds. Your total funds are €" + str(account_total))
                elif bet <= 0:
                    print("Cannot be les than 1 i'm afriad")
                else:
                    bet_correct = True
                    account_total -= bet
                    print("You bet: €{}".format(bet))
        return bet
                
    def single_deck_play():
        global player_bet
        global player_card_value    
        new_bet_input = correct_bet() 
        if new_bet_input == type(str) and new_bet_input == "no" or new_bet_input =="n":
            pass
        else:
            player_bet += new_bet_input
            print("Your new amount is: €" + str(player_bet))
        
    
    def pull_card():
        pull_card_1 = Card(cr(), nr())
        pull_card_1.create_card()
        return pull_card_1.cards[-1]

    def split_play():
        global player_cards_1
        global player_card_value
        global player_card_value_1
        global account_total
        if player_cards[0] == player_cards[1]:
            x = input("You have double cards. Would you like to split? (y/n)")
            if x == "y":
                player_cards_1.append(player_cards[-1])
                del player_cards[-1]
                new_card_1 = pull_card()
                new_card_2 = pull_card()
                player_cards.append(new_card_1)
                player_cards_1.append(new_card_2)
                print("\nThese are your new decks:\nDeck one")
                for card in player_cards:
                    player_card_value += int(card[-1])
                    print("The {num} of {color}".format(num=card[1].title(), color=card[0].title()))
                print("\nDeck Two")   
                for card in player_cards_1:
                    player_card_value_1 += int(card[-1])
                    print("The {num} of {color}".format(num=card[1].title(), color=card[0].title()))
                if player_card_value == 21 or player_card_value_1 == 21:
                        account_total += player_bet *3
                        print("Blackjack! You won: {num}".format(num=int(player_bet *3)))   
                        main() 
            else:
                pass
        return player_cards_1   

    def double_deck_play():
        global player_bet
        global player_bet_1
        global player_card_value    
        global player_card_value_1
        global account_total
        conf_bet_1 = input("Would you like to place a new bet on deck one? (y/n)\n")
        if conf_bet_1.lower() == "y" and account_total > 0:
            new_bet_input = correct_bet() 
            if new_bet_input == type(str) and new_bet_input == "no" or new_bet_input =="n":
                pass
            else:
                player_bet += new_bet_input
                print("Your new amount is: €" + str(player_bet))
        elif conf_bet_1.lower() == "y" and account_total <= 0:
            print("\nInsufficient funds\n")
            pass
        else:
            pass

        conf_bet_2 = input("Would you like to place a new bet on deck one? (y/n)\n")
        if conf_bet_2.lower() == "y" and account_total > 0:
            new_bet_input = correct_bet() 
            if new_bet_input == type(str) and new_bet_input == "no" or new_bet_input =="n":
                pass
            else:
                player_bet_1 += new_bet_input
                print("Your new amount is: €" + str(player_bet))
        elif conf_bet_2.lower() == "y" and account_total <= 0:
            print("\nInsufficient funds\n")
            pass
        else:
            pass

        new_card_input = input("\nWould you like to pull another card for deck one? (y/n\n")
        while new_card_input.lower() == "y":   
            new_card = pull_card()
            player_cards.append(new_card)
            player_card_value += new_card[-1]
            print("\nYour new card is: \nThe {num} of {color}".format(num=new_card[1].title(), color=new_card[0].title()))
            for card in player_cards:
                if "ace" in card and player_card_value > 21:
                    player_card_value -= 10
                    card.pop(1)
                else:
                    pass
            if player_card_value > 21:
                account_total -= player_bet
                print("\nYou bust. The bank wins!")
                main()
            elif player_card_value == 21:
                account_total += player_bet *3
                print("\nBlackjack! You win {}".format(str(player_bet *3)))
                main()
            else:
                new_card_input = input("\nWould you like to pull another card for deck one? (y/n\n")
        else:
            pass

        new_card_input = input("\nWould you like to pull another card for deck one? (y/n\n")
        while new_card_input.lower() == "y":   
            new_card = pull_card()
            player_cards_1.append(new_card)
            player_card_value_1 += new_card[-1]
            print("\nYour new card is: \nThe {num} of {color}".format(num=new_card[1].title(), color=new_card[0].title()))
            for card in player_cards_1:
                if "ace" in card and player_card_value_1 > 21:
                    player_card_value_1 -= 10
                    card.pop(1)
                else:
                    pass
            if player_card_value_1 > 21:
                account_total -= player_bet_1
                print("\nYou bust. The bank wins!")
                main()
            elif player_card_value_1 == 21:
                account_total += player_bet_1 * 3
                print("\nBlackjack! You win {}".format(str(player_bet_1 *3)))
                main()
            else:
                new_card_input = input("\nWould you like to pull another card for deck one? (y/n\n")
        else:
            pass

    def bank_pulls_first_cards():
        global player_bet, player_bet_1, player_card_value, player_card_value_1, account_total
        bank_cards = []
        bank_score = 0
        print("\nThe bank pulls the following cards:\n")
        for i in range(2):
            bank_card_1 = pull_card()
            bank_cards.append(bank_card_1)
            bank_score += bank_card_1[-1]
            print("The {num} of {color}".format(num=bank_card_1[1].title(), color=bank_card_1[0].title()))
            if player_card_value_1 > 0:
                if bank_score > player_card_value_1:
                    account_total -= player_bet_1
                    player_card_value_1 = 0
                    print("\nThe bank wins deck two! You lost: €{}".format(player_bet_1))
                elif bank_score > player_card_value:
                    account_total -= player_bet
                    player_card_value = player_card_value_1
                    player_bet = player_bet_1
                    player_card_value_1 = 0
                    print("\nThe bank wins deck one! You lost: €{}".format(player_bet))
                elif bank_score > player_card_value and bank_score > player_card_value_1:
                    account_total -= player_bet + player_bet_1
                    print("\nThe bank wins both decks! You lost: €{}".format(player_bet_1 + player_bet))
                    main()
                else:
                    pass
            elif bank_score > player_card_value:
                account_total -= player_bet
                print("\nThe bank wins! You lost €{}".format(player_bet + player_bet_1))
                main()
            elif bank_score <= player_card_value:
                account_total += player_bet *2
                print("\nCongratulations! You win €{}".format(player_bet + player_bet_1))

        while bank_score < 17:
            bank_card_add = pull_card()
            bank_cards.append(bank_card_add)
            bank_score += bank_card_add[-1]
            print("\nThe bank pulls:\nThe {num} of {color}".format(num=bank_card_add[1].title(), color=bank_card_add[0].title()))
            for card in bank_cards:
                if "ace" in card and bank_score > 21:
                    bank_score -= 10
                    card.pop(1)
                else:
                    pass
            if player_card_value_1 > 0:
                if bank_score >= 22:
                    account_total += (player_bet + player_bet_1) *2
                    print("\nThe bank busts! You win: €{}".format((player_bet + player_bet_1) *2))
                elif bank_score > player_card_value_1 and bank_score > player_card_value:
                    account_total -= player_bet + player_bet_1
                    print("\nThe bank wins! You lost €{}".format(player_bet + player_bet_1))
                elif bank_score <= player_card_value_1 and bank_score <= player_card_value:
                    account_total += (player_bet + player_bet_1) *2
                    print("\nYou win! Congratulations. Here is: {}".format((player_bet + player_bet_1) *2))
                elif bank_score > player_card_value_1:
                    account_total -= player_bet_1
                    print("\nThe bank wins deck two! You lost: €{}".format(player_bet_1))
                elif bank_score > player_card_value:
                    account_total -= player_bet
                    print("\nThe bank wins deck one! You lost: €{}".format(player_bet))
                elif bank_score > player_card_value and bank_score <= player_card_value_1:
                    account_total += player_bet_1 - player_bet
                    print("\nThe bank wins deck one but loses deck two! Your funds will recieve: €{}".format(player_bet_1 + player_bet))
                elif bank_score <= player_card_value and bank_score > player_card_value_1:
                    account_total += player_bet - player_bet_1
                    print("\nThe bank wins deck two but loses deck one! Your funds will recieve: €{}".format(player_bet_1 + player_bet))
                else:
                    pass
            elif bank_score >= 22:
                account_total += player_bet *2
                print("\nThe bank busts! You win: €{}".format(player_bet *2))
            elif bank_score > player_card_value:
                account_total -= player_bet
                print("\nThe bank wins! You lost €{}".format(player_bet))
            else:
                account_total += player_bet * 2
                print("\nYou win! Congratulations. Here is: {}".format(int(player_bet *2)))
        main()


    new_game_confirm = input("\nYou have €" + str(account_total) + " in funds.\nAre you ready to play another game? (y/n)\n")
    if new_game_confirm.lower() == "y" or new_game_confirm.lower() == "yes":
        new_game()
        print("Fantastic! Let's begin!\n")
        print("Please place your bet!")
    elif new_game_confirm.lower() == "n" or new_game_confirm.lower() == "no":
        print("Sorry to hear that. Untill next time!")
        exit()
    else:
        print("\nPlease enter a valid response")
        main()

    bet_1 = correct_bet()
    player_bet += bet_1
    print("\nThese are your cards:\n")
    for i in player_cards:
        player_card_value += i[2]
        print("The {num} of {color}".format(num=i[1].title(), color=i[0].title()))
        if player_card_value == 21:
            account_total += player_bet *3
            print("\nBlackjack!\n \nYou won {}".format(player_bet *3))
            main()

    player_cards_1 = split_play()

    if player_card_value_1 == 0:
        bet_new = False
        if account_total <= 0:
            bet_new = True
        while bet_new == False:
            bet_yn = input("\nYou have €" + str(account_total) + "\nWould you like to place a new bet? Your current bet is €" + str(player_bet) + " (y/n)\n")
            if bet_yn.lower() == "y" or bet_yn.lower() == "yes":
                print("\nPlease place your new bet:")
                bet_new = True
                single_deck_play()
            elif bet_yn.lower() == "n" or bet_yn.lower() == "no":
                bet_new = True
                pass
            else:
                print("Please enter yes (y) or no (n)")
    else:
        double_deck_play()

    if player_card_value_1 == 0:
        new_card_input = input("\nWould you like to pull another card? (y/n)\n")
        while new_card_input.lower() == "y":   
            new_card = pull_card()
            player_cards.append(new_card)
            player_card_value += new_card[-1]
            print("\nYour new card is: \nThe {num} of {color}".format(num=new_card[1].title(), color=new_card[0].title()))
            for card in player_cards:
                if "ace" in card and player_card_value > 21:
                    player_card_value -= 10
                    card.pop(1)
                else:
                    pass
            if player_card_value > 21:
                print("\nYou bust. The bank wins!")
                main()
            elif player_card_value == 21:
                print("\nBlackjack! You win {}".format(str(player_bet *3)))
                main()
            else:
                new_card_input = input("\nWould you like to pull another card? (y/n\n")
        else:
            pass

        bank_pulls_first_cards()
while account_total > 0:
    main()        
else:
    print("No more funds. See you next time!")
    exit()







