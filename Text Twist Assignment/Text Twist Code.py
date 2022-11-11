#Steven Rud
import random
import itertools

with open('words7.txt') as file: #opening the file and splitting it into every word
    words=file.read().split()
    #print(words)
    
seven=[]   #defining a list to later add all 7 letter words in 
def main():
    for i in range(len(words)): #for loop in range of all words to check every word
        if len(words[i])==7: #filtering only 7 letter words
            seven.append(words[i]) #adding the words to the list
    clue=random.choice(seven) #defines the random 7 letter word
    #print(clue)
    answers=getallwords(clue) #defines answers so it can be used later all possible words in the 7 letter word from the getallwords function
    twist(clue,answers)

                    
def getallwords(clue):  #places all the words that can be made from clue into a list and returns list
    final=[]
    for n in range(3,8):
        final.extend(getwords(clue,n))        
    return final
    
    

def getwords(clue,n): 
    allwords=[] 
    x=list(map("".join, itertools.permutations(clue, n))) #defines x as a list of all posible permuations for the clue
    for i in range(len(x)):
        if len(x[i])==n: #checks for all possible length in range
            if x[i] not in allwords and x[i] in words:  #adds all the permutations in x that aren't already there and are words from the file to the list allwords
                allwords.append(x[i])
    allwords.sort() #sorts it correctly
    #print(allwords)
    return allwords
                
        
   
def twist(clue,answers):
    guesses=set() #defines set of guesses to add all user inputs into
    guess='a' #defines the input of the user
    z=list(clue) #converts string of clue to a list
    random.shuffle(z) #scambles it
    count=0 #defines count of all correct answers
    while guess!='q' and count!=len(answers): #check if input isn't q and that all words weren't answered 
        printboard(z,guesses,answers)
        guess=input('Guess a word, or q for quit or t for twist: ')
        guesses.add(guess) #adds guess input to set
        if guess in answers: 
            count+=1 #adds for each correct input
        if guess=='t': #Randomizes clue
            random.shuffle(z)
    if guess=='q' or count==len(answers): #prints final message when finished
        print("Thanks For playing!")
            
    
    
def printboard(clue,guesses,answers): #prints board and adds answers to board when inputted
    for i in range(len(answers)):
        if answers[i] in guesses:
            print(answers[i])
        else:
            print('_ '*len(answers[i]))
    shuffle=''.join(clue)
    print()
    print(shuffle)  #prints scambled word
        
    
main()