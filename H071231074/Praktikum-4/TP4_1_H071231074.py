def stringPermutation(word):
    try:
        huruf = word
        for i in range(len(word)):
            permutations = huruf[-1] + huruf[0:-1] 
            print(permutations, end="|")
            huruf = permutations
    except:
        print("Type Error")

# Test Case 1
stringPermutation("Mobil")
print()

# Test Case 2
stringPermutation("Ayam")
print()

# Test Case 3
n = input("Masukkan kata = ")

if type(n) == str:
    stringPermutation(n)
elif n != str:
    print("Type Error")
