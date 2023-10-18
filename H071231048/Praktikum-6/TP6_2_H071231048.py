
def input_array():
    array1 = input("Input array ke-1: ")
    array2 = input("Input array ke-2: ")

    array1 = list(map(int, array1.split()))
    array2 = list(map(int, array2.split()))
    duplicate_data = [velue for velue in array1 if velue in array2]
    return duplicate_data

def program_array():
    duplicate = input_array()
    if duplicate:
        print(f"Terdapat {len(duplicate)}, buah duplicate yaitu {tuple(duplicate)}")
    else:
        print("Tidak ada duplicate")

program_array()

