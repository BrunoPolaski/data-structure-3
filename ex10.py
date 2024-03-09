wordsWithACounter = 0

def wordsStartingWithA(words):
    for word in words:
        if word[0] == 'a':
            wordsWithACounter += 1

wordsStartingWithA(["apple", "banana", "avocado"])

print(wordsWithACounter)