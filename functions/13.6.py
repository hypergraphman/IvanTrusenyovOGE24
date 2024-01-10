def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False

    k = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            k += 1

    return k == 1


txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))