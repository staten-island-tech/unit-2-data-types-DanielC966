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

"""
def determineTip(billValue, service):
    if service == "bad":
        total = billValue
        tip = total - billValue
        print("Total: $" + str(total))
        print(f"Tip: {tip} (No tip)")

    elif service == "okay":
        total = billValue + (billValue * 0.15)
        print("Total: $" + str(total))
        tip = total - billValue
        print(f"Tip: {tip} (0.15%)")

    elif service == "good":
        total = billValue + (billValue * 0.2)
        print("Total: $" + str(total))
        tip = total - billValue
        print(f"Tip: {tip} (0.20%)")

    elif service == "great":
        total = billValue + (billValue * 0.25)
        print("Total: $" + str(total))
        tip = total - billValue
        print(f"Tip: {tip} (0.25%)")

determineTip(15, "bad")
"""

#Challenge: Find Factors

"""
number = int(input("Input number: "))

def determineFactors(x):
    factorList = []
    
    for i in range(1, x+1):
        if x%i < 1:
            factorList.append(i)

    print(factorList)

determineFactors(number)
"""

#Challenge: Greatest Common Factor

def findGCF(x, y):
    greatestX = 0
    greatestY = 0

    for i in range(x+1) and range(y+1):
        if i > greatestX  and i > greatestY:
            greatestX = i
            greatestY = i
            if x%greatestX ==0 and y%greatestX==0:
                gcf = greatestX
    print(f"GCF: {gcf}")

findGCF(28, 42)