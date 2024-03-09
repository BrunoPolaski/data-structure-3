def sameWords(list1, list2: list) -> list:
    wordsInCommon = []
    for word in range(len(list1)):
        for word2 in range(len(list2)):
            if list1[word] == list2[word2]:
                wordsInCommon.append(list1[word])
    return wordsInCommon

print(sameWords(["apple", "banana", "avocado"], ["banana", "avocado", "grapefruit"]))