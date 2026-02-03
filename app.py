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
"""
firstAdj = input("Input an adjective: ")
secondNoun = input("Input a character: ")
thirdVerb = input("Input a verb (-ing): ")
fourthVerb = input("Input another verb (past tense): ")
print(f"It was a {firstAdj} day in the park when {secondNoun} unexpectedly caught his dad {thirdVerb} the dog. Then, {secondNoun} {fourthVerb} into the pond.")
"""

#Problem 2
"""
def discount(age, isResident, isMember):
    if age < 12 or age >= 65:
        print("dicoiunt givne")
    elif isResident == True or isMember == True:
        print("discount granted")
    else:
        print("NOOOOOO discount")

discount(26, False, True)
"""

#Challenge: Odd or Even

"""
def checkNumber(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")

checkNumber(35)

"""

#Challenge: Bill Tip

def determineTip(billValue, service):
    if service == "bad":
        print(billValue)
    elif service == "okay":
        billValue = billValue + (billValue * 0.15)
        print(billValue)
    elif service == "good":
        billValue = billValue + (billValue * 0.2)
        print(billValue)
    elif service == "great":
        billValue = billValue + (billValue * 0.25)

determineTip(15, "great")