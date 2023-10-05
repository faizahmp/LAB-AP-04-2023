input = input("Masukkan kata=")
def stringPermutation(input):
    if input.isnumeric():
        raise "input must be string for string permutation"
    else:
        try:
            hasil = []
            for i in range(1, len(input)+1):
                mutasi = input[-i:]+input[:-i]
                hasil.append(mutasi)
            return " | ".join(hasil)
        except TypeError :
            print("invalid input")
output = stringPermutation(input)
print(output + " | ")
        
