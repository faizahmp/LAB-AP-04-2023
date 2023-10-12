def create_new_string(input_string):
    length = len(input_string)

    # Pastikan panjang string cukup untuk mengambil karakter pertama, tengah, dan terakhir
    if length < 3:
        return "Panjang string tidak mencukupi"

    middle_index = length // 2

    # Ambil karakter pertama, tengah, dan terakhir
    new_string = input_string[0] + input_string[middle_index] + input_string[-1]

    return new_string

# Contoh penggunaan
input_string = input()
new_string = create_new_string(input_string)
print(new_string)
