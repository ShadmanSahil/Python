import random

class game:
    deck=[]
    suits=['hearts','diamonds','clubs','spades']

    p1=[]
    p2=[]
    p3=[]
    p4=[]

    p_1=0
    p_2 = 0
    p_3 = 0
    p_4=0

    names=[]
    val=[]
    suit=[]

    # creating deck
    for i in range(len(suits)):
        for k in range(1,14):
            deck.append('{} of {}'.format(k,suits[i]))

    # deals each player different cards every game
    def deal(self):
        while len(self.p1)!=13:
            a=random.randint(1,13)
            b=random.choice(self.suits)
            z='{} of {}'.format(a,b)
            if z not in self.p1:
                self.p1.append(z)
        while len(self.p2)!=13:
            a=random.randint(1,13)
            b=random.choice(self.suits)
            z='{} of {}'.format(a,b)
            if z not in self.p1 and z not in self.p2:
                self.p2.append(z)
        while len(self.p3)!=13:
            a=random.randint(1,13)
            b=random.choice(self.suits)
            z='{} of {}'.format(a,b)
            if z not in self.p1 and z not in self.p2 and z not in self.p3:
                self.p3.append(z)
        while len(self.p4)!=13:
            a=random.randint(1,13)
            b=random.choice(self.suits)
            z='{} of {}'.format(a,b)
            if z not in self.p1 and z not in self.p2 and z not in self.p3 and z not in self.p4:
                self.p4.append(z)

    # removes all elements from each hand for new shuffle and deal
    def restart(self):
        self.p1=[]
        self.p2 = []
        self.p3 = []
        self.p4 = []

        self.p_4=0
        self.p_3=0
        self.p_2=0
        self.p_1=0

    # checking round scores
    def check(self):
        for i in range(len(self.suit)):
            if self.suit[i]!=self.suit[0] and self.suit[i]!='spades':
                self.val[i]=0
            if self.suit[i]=='spades':
                self.val[i]=self.val[i]*100
        x=self.val.index(max(self.val))
        if x==0:
            self.p_1=self.p_1+ 1
        elif x==1:
            self.p_2=self.p_2+ 1
        elif x==2:
            self.p_3=self.p_3+ 1
        elif x==3:
            self.p_4=self.p_4+ 1
        self.val=[]
        self.suit=[]

    # ending game, declaring winner
    def end(self):
        scores=[]
        scores.append(self.p_1)
        scores.append(self.p_2)
        scores.append(self.p_3)
        scores.append(self.p_4)
        if self.p_1==max(scores):
            print('player 1 wins!!!')
        elif self.p_2==max(scores):
            print('player 2 wins!!!')
        elif self.p_3==max(scores):
            print('player 3 wins!!!')
        elif self.p_4==max(scores):
            print('player 4 wins!!!')
        print('Thanks for playing')

    # allows players to see scores
    def see_score(self):
        scores=[]
        scores.append(game.p_1)
        scores.append(game.p_2)
        scores.append(game.p_3)
        scores.append(game.p_4)
        for i in range(len(self.names)):
            print(self.names[i],scores[i])


class player:

    def __init__(self,name):
        self.name=name
        game.names.append(self.name)

    # player draws a list. others re-arrange, ensuring everyone is not drawing same list
    def draw(self):
        self.hand=game.p1
        game.p1=game.p2
        game.p2=game.p3
        game.p3=game.p4

    # shows all the cards of a player
    def show(self):
        print(self.name,':',self.hand)

    # player plays the card
    def play(self,val,suit):
        game.val.append(val)
        game.suit.append(suit)
        card='{} of {}'.format(val,suit)
        self.hand.remove(str(card))

