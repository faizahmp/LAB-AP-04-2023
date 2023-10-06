def palindrome(word: str) -> str:
    # Menghilangkan spasi dan mengubah huruf menjadi huruf kecil
    word = word.replace(" ", "").lower()
    
    # Memeriksa apakah kata sama dengan kata terbaliknya
    if word == word[::-1]:
        return print("Palindrom")
    else:
        return print("Bukan Palindrom")

# Test Case 1
result1 = palindrome("Radar")

# Test Case 2
result2 = palindrome("Step on no pets")

# Test Case 3
palindrome(input("Masukkan Kata = "))