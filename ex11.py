def wordsWithMoreThanThreeLetters(words):
    words = []
    for word in words:
        if len(word) > 3:
            words.append(word)
    return words

print(wordsWithMoreThanThreeLetters(["apple", "banana", "avocado"]))