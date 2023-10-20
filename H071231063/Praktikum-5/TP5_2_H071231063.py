def create_new_string(input_string):
    panjang = len(input_string)
    if panjang < 3:
        return "Panjang string tidak mencukupi"
    middle_index = panjang // 2
    new_string = input_string[0] + input_string[middle_index] + input_string[-1]
    return new_string
input_string = input("Masukkan kata: ")
new_string = create_new_string(input_string)
print(new_string)