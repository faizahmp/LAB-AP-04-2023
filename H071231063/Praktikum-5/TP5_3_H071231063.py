def are_anagrams(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    return sorted(word1) == sorted(word2)

# Contoh penggunaan
word1 = "Astronomer"
word2 = "Moon Starer"
result = are_anagrams(word1, word2)
print(result)  # Output: True
