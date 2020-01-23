import random


class Deck:
    def __init__(self, Packs, Ranks):
        self.Packs = Packs
        self.Ranks = Ranks

    def __print__(self):
        return self.Ranks + " in " + self.Packs


class BlackJack:
    def __init__(self, player, dealer, card, value):
        self.player = player
        self.dealer = dealer
        self.card = card
        self.value = value

    def __random__(self, Contestant):
        contestant_AceCount, contestant_sum = 0, 0
        for _ in range(0,2):
            random.shuffle(self.card)
            pulled_card = self.card.pop()
            Contestant.append(pulled_card)
            if pulled_card.Ranks == 'Ace':
                contestant_AceCount += 1
            contestant_sum += self.value[pulled_card.Ranks]
        return contestant_AceCount, contestant_sum

    def __print__(self):
        print("Player has 2 cards:")
        for playerCard in self.player:
            print(playerCard.__print__())
        print("Dealer is showing you one of his cards.")
        carder = random.randint(0, 1)
        print(self.dealer[carder].__print__())

    def hit(self, contestant, contestant_sum):
        random.shuffle(self.card)
        pulled_card = self.card.pop()
        contestant.append(pulled_card)
        contestant_sum += self.value[pulled_card.Ranks]
        return contestant_sum

def showallcards(Player, Dealer):
    print("\n\nPlayer Cards")
    for playerCard in Player:
        print(playerCard.__print__())
    print("\nDealer Cards")
    for dealerCard in Dealer:
        print(dealerCard.__print__())

def accounttransfer(ContestantBet, isPlayerWon):
    global playerAccount
    global dealerAccount
    if isPlayerWon:
        playerAccount += ContestantBet
        dealerAccount -= ContestantBet
    elif not isPlayerWon:
        playerAccount -= ContestantBet
        dealerAccount += ContestantBet

    print("\nPlayer Account has ",playerAccount)
    print("Dealer Account has ", dealerAccount)


def sumofcontestants(value, contestant):
    contestant_sum = 0
    for aCard in contestant:
        contestant_sum += value[aCard.Ranks]
    return contestant_sum


def checkthewinner(Contestant1, Contestant2, PlayerBet, DealerBet, Player, Dealer):
    if Contestant1 > Contestant2:
        print("\n\nPLAYER WON THE MATCH!")
        showallcards(Player, Dealer)
        accounttransfer(DealerBet, True)
    elif Contestant2 > Contestant1:
        print("\n\nDEALER WON THE MATCH!")
        showallcards(Player, Dealer)
        accounttransfer(PlayerBet, False)
    elif Contestant1 == Contestant2:
        print("\n\nIT'S A DRAW MATCH")


def __maingame__(values, cards):
    Player, Dealer = [], []
    black_jack = BlackJack(Player, Dealer, cards, values)
    pAceCount, sum_player = black_jack.__random__(Player)
    dAceCount, sum_dealer = black_jack.__random__(Dealer)
    black_jack.__print__()
    print("Players Sum of cards is:", sum_player)
    playerBet = int(input("How much Bet Amount you are going to place:"))
    global playerAccount

    while playerBet > playerAccount:
        print("Sorry, your bet amount can't exceed your bank balance ",playerAccount)
        playerBet = int(input("Please place your bet amount:"))

    if playerAccount // 2 < playerBet:
        print("Please place the bet amount less than half of the Bank balance for your 'SAFETY'")
        playerBet = int(input("Please place your bet amount:"))
    dealerBet = int(playerBet * 1.5)
    playactive, playerplaying, dealerplaying = True, True, False
    choose4or5 = True
    n = 2

    while playactive:
        while playerplaying:
            print("\n\n'OPTIONS':\n---------\n1.HIT\n2.STAND\n3.SHOW")
            if choose4or5: print("4.DOUBLE")
            choice = int(input("Choose any one of the options:"))
            if choice == 1 or choice == 4:
                if choice == 4 and choose4or5:
                    print("\nPlayer want to double the bet amount")
                    playerBet, dealerBet = playerBet*2, dealerBet*2
                    choose4or5 = False
                elif choice == 4 and not choose4or5:
                    print("Choose The correct option from given.")
                    break

                print("\nPlayer is going to take a card.")
                sum_player = black_jack.hit(Player, sum_player)
                print(Player[n].__print__())
                n += 1
                print("\nSum of Cards is ",sum_player)
                playerplaying, dealerplaying = False, True
                if sum_player > 21 and pAceCount:
                    sum_player -= 10
                    pAceCount -= 1
                    print("Player have an 'Ace' card" + "\nPlayer's sum of cards is ",sum_player)
                elif sum_player > 21 and not pAceCount:
                    dealerplaying, playactive = False, False
                    print("\nDEALER WON THE MATCH!")
                    showallcards(Player, Dealer)
                    print("\n\nPlayer Total sum of cards:", sum_player)
                    print("Dealer Total sum of cards:", sum_dealer)
                    accounttransfer(playerBet, False)

            elif choice == 2:
                print("\nPlayer want to skip his turn.")
                playerplaying, dealerplaying= False, True

            elif choice == 3:
                print("\nLet's end this game.")
                print("Player Total sum of cards:", sum_player)
                print("Dealer Total sum of cards:", sum_dealer)
                checkthewinner(sum_player, sum_dealer, playerBet, dealerBet, Player, Dealer)
                playerplaying, playactive = False, False
                
            else:
                print("Choose The correct option from given.")

        while dealerplaying:
            if sum_dealer < 17:
                print("\nDealer is going to take a card.")
                sum_dealer = black_jack.hit(Dealer, sum_dealer)
                playerplaying, dealerplaying = True, False
                if sum_dealer > 21 and dAceCount:
                    sum_dealer -= 10
                    dAceCount -= 1
                elif sum_dealer > 21 and not dAceCount:
                    playerplaying, playactive = False, False
                    print("\nPLAYER WON THE MATCH!")
                    showallcards(Player, Dealer)
                    print("Player Total sum of cards:", sum_player)
                    print("Dealer Total sum of cards:", sum_dealer)
                    accounttransfer(dealerBet, True)

            elif sum_dealer <= 21:
                print("\nDealer will skip his chance.")
                playerplaying = True
                dealerplaying = False


if __name__ == '__main__':
    Pack = ['Heart', 'Spade', 'Club', 'Diamond']
    Rank = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Ace', 'Jack', 'Queen', 'King']
    Values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    Card = []
    for pack in Pack:
        for rank in Rank:
            Card.append(Deck(pack, rank))
    playerAccount, dealerAccount = 100000, 10000000
    print("Cash in Player Account:", playerAccount, "\n\n")
    __maingame__(Values, Card)

    game = True
    while game and playerAccount > 1000:
        playagain = input("Do You Want To This Game Again (Yes/No):").lower()
        if playagain[0] == 'y' and playerAccount > 1000:
            print("\n\nCash in Player Account:", playerAccount, "\n\n")
            __maingame__(Values, Card)
        elif playagain[0] == 'n':
            print("\n\n\nTHANKS FOR PLAYING THIS GAME")
            exit(0)
    else:
        print("You can't continue to play this game, Because of your inSufficient Funds in your Bank Account.")
