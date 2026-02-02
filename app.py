#Challenge 1: Word Count

"""
sentence = input("Input a sentence: ")

def wordCounter(sentence):
    s = sentence
    wordList = s.split()
    counted = 0
    for i in wordList:
        counted +=1
    
    return counted

print(str(wordCounter(sentence)) + " words")
"""

#Challenge 2: Mad Libs

firstAdj = input("Input an adjective: ")
secondNoun = input("Input a character: ")
thirdVerb = input("Input a verb (-ing): ")
fourthVerb = input("Input another verb (past tense): ")
print(f"It was a {firstAdj} day in the park when {secondNoun} unexpectedly caught his dad {thirdVerb} the dog. Then, {secondNoun} {fourthVerb} ")
