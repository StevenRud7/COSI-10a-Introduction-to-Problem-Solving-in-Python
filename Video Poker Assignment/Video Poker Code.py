#Steven Rud
import random

SUITS=u'\u2660'+u'\u2665'+u'\u2666'+u'\u2663'

deck=[] #empty global list so deck can be used in functions

hands={} #the hand names dictionary
hands[1]='Busted'
hands[2]='Jacks or Better Pair'
hands[4]='Two Pair'
hands[8]='Three of a kind'
hands[9]='Straight'
hands[10]='Flush'
hands[16]='Full House'
hands[64]='Four of a kind'
hands[90]='Straight Flush'
hands[110]='Royal Flush'

payouts={} #the winnings dictionary 
payouts[1]=-1
payouts[2]=1
payouts[4]=2
payouts[8]=4
payouts[9]=6
payouts[10]=8
payouts[16]=15
payouts[64]=25
payouts[90]=40
payouts[110]=50



def main():
    stake=100 #defines stake and bet
    prevbet=10
    while stake>0:
        bet=getbet(stake,prevbet)
        if bet==0: #checks for the quit input and if yes ends the loop and returns your balance
            print('Thank you for playing. You are exiting with $',stake)
            return
        deck=newdeck() #define and call each function
        hand=deal(deck)
        select(hand)
        #draw(deck,hand)
        factor=rate(hand)
        stake=stake+(int(bet)*payouts[factor])
        prevbet=bet
        print('Your hand is:',hands[factor]) #prints the hand
        print('You win',int(bet)*payouts[factor]) #prints the payout
    if stake<=0: #checks if I ran out of money and then if true ends the loop.
        print('Thank you for playing. You are exiting with $0')
        return
    

def getbet(stake,prevbet): #the get bet function checks the various inputs for the bet.
    while True:
        #print('You have',stake,end=' ')
        bet=input('You have '+ str(stake)+ '. whats your bet (0 to quit)? ['+str(prevbet)+'] ')
        if bet=='': #if blank than it is the same as the previous bet
            #stake=prevbet
            return prevbet
        elif int(bet)>stake: #if over my balance it calls for a new input
            print("You don't have that much!")
        elif int(bet)!=0 and int(bet)<stake: #if a normal situation returns the bet value
            #stake=stake-bet
            return bet
        elif int(bet)==stake: #if bet is my balance than prints risky
            print('Risky')
            return bet
        elif int(bet)==0: #if 0 to quit then it returns 0 to later terminate in the main
            return 0
        

    

def newdeck(): #creates the deck with a nested for loop
    for i in range(1,14): #creates the 1-13 numbers
        for j in range(1,5):  
            x=i+(j/10)
            deck.append(x) #creates the 0.1-0.4 numbers to be added to the 1-13 numbers
    #print(deck)
    random.shuffle(deck)
    return deck

def deal(deck): #deal each card inddivually 
    c1=deck.pop(0)
    c2=deck.pop(0)
    c3=deck.pop(0)
    c4=deck.pop(0)
    c5=deck.pop(0)
    return [c1,c2,c3,c4,c5]

def printhand(hand):
    for i in range(5): #Replaces the called postion with a blank space if value for postion is negative
        if hand[i]<0:
            print('  ',end='')
        else:    #prints other cards normally
            printcard(hand[i]) 



def select(hand):
    flag=True
    while flag:
        printhand(hand)
        choice=int(input('Enter 1 thru 5 to discard (or recover) a card, 0 to draw! '))
        if choice!=0:
            hand[choice-1]= -hand[choice-1] #converts the position called to a negative value to be replaced with a blank space in printhand
        else:
            flag=False        
    return draw(deck,hand)

    #printhand(hand)
    

def draw(deck,hand): #fills in the empty places with a new card
    #print(hand)
    for i in range(5):
        if hand[i]<0: #checks if negative
            hand[i]=deck.pop(0) #pops in a new card
    printhand(hand)
    return hand




def printcard(card):
    print('A23456789TJQK'[int(card)-1],SUITS[frac(card)-1],sep='',end=' ')

def frac(card):
    return round(card %1 * 10)

def rate(hand):  #sort and rate a poker hand
    shand=sorted(hand)
    i,j,prod = 0,1,1
    while j < 5:
        if int(shand[i]) == int(shand[j]):
            prod=prod*2**(j-i)
            c=int(shand[j])  #what card made the 2,3,4 of a kind
        else:
            i=j
        j+=1
    if prod == 1: #check for straight and flush and high strait
        d,f,e = 9,10,11
        for i in range(1,5):
            d = 1 if int(shand[i]) != int(shand[i-1])+1 else d
            e = 1 if int(shand[i]) != 8+i+int(shand[0]) else e
            f = 1 if frac(shand[0]) != frac(shand[i]) else f
        prod=d*e*f
    prod = 9 if prod == 11 else prod # there aint no high strait
    prod = 1 if prod == 2 and 1 < c < 11 else prod #jacks or better
    return prod

main() #call main