def arrayStringsAreEqual( word1, word2):
    word1 = ""
    word2 = ""
        
    for word in word1:
        word1 += word1
            
    for newword in word2:
        word2 += newword

    print(word1)
    print(word2)
            
    if word1 == word2:
        return True
    else:
        return False

result = arrayStringsAreEqual(["a", "cb"], ["ab","c"])
print(result)