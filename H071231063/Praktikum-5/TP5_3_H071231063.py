def are_anagrams(kata1, kata2):
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()
    if len(kata1) != len(kata2):
        return False
    char_count = {}
    for char in kata1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        print(char_count)
    for char in kata2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False
    return all(count == 0 for count in char_count.values())
kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")
result = are_anagrams(kata1, kata2) 
print(result)