#Steven Rud
import random

FILE='''I am typing a bit of nonsense in order to test my text justification program. The goal is to split a file into paragraphs using a unique separator,
and then for each paragraph, split it into lines and add spaces so the each line prints the same length.

We are ignoring punctuation and carriage returns.
The only caveat is that if the last line only has one word in it, it should be left justified.

The goal of the program is to be a primitive simulation of one of the functions of a word processor, the most ubiquitous of software applications which used to have a vibrant ecosystem of variants, but which has collapsed into a monopoly governed by Microsoft word.
Other parts of word processing require paging files into buffers, spell checking, display management and keyboard processing.'''



def printpara(words,length):   #the printpara function defines lines and spaces and as calls the other functions
    while len(words)!=0:
        line=getline(words,length)        
        spaces=[]
        for i in range(0,len(line)-1):
            spaces.append(1)
        spaces.append(0)
        Addspace(line,spaces,length)    
        printline(line,spaces)
        
def Addspace(line,spaces,length): #Addspace function first finds total length of line and then compares with the wanted length (40 or 60)
    total=0
    for i in range(len(line)):
        total+=len(line[i])
        total+=spaces[i]
    while total<length: #use randint to place extra spaces into the line
        spot=random.randint(0,len(spaces)-2) #defines random possible place to add the space without inculding the end
        spaces[spot]+=1
        total+=1
        
                
def getline(words,length): #getline function was given and it adds the words to the list while keeping track of the word's length
    ans=[]
    total=0
    while (length>total) and 0 != len(words):
        word=words.pop(0)
        total += len(word)+1  #add 1 for the space
        ans.append(word)
        #now we are one word too long
    if total > length:
        words.insert(0,ans.pop())
    return ans

def printline(line,spaces):  # This uses a nested for loop to print each line with the correct number of spaces and words
    for i in range(len(line)):
        print(line[i], end='')
        for j in range(spaces[i]):
            print(' ',end='')
    print()

def main(length):    # this is the main function which creates the initial split and defines words for each word in the string
    p=FILE.split("\n\n")
    for i in range(len(p)):        
        words=p[i].split()
        print() #Adds a gap between the paragraphs
        printpara(words,length) # call the printpara function which later calls the rest of the functions.
    
main(40)    #calls main function with a 40 length
print()
print()
main(60)    #calls main function with a 60 length    
    