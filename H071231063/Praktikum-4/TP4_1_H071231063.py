def stringPermutation(word):
    try:
        n=int(word)
        print("inputan tidak valid")
    except:
        for i in range(len(word)):
            word = word[-1]+word[:-1] 
            print(word,end="|")
input_word = input("Masukkan kata: ")
stringPermutation(input_word)