def is_palindrome(word: str) -> str:
    word = word.replace(" ", "").lower()
    if word == word[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"
input_word = input("Masukkan sebuah kata: ")
result = is_palindrome(input_word)
print(result)