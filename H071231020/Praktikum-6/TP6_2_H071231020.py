# def input_array():
#     array1 = input("Input array ke-1: ")
#     array2 = input("Input array ke-2: ")

#     array1 = list(map(int, array1.split()))
#     array2 = list(map(int, array2.split()))
#     duplicate_data = [velue for velue in array1 if velue in array2]
#     return duplicate_data

# def program_array():
#     duplicate = input_array()
#     if duplicate:
#         print(f"Terdapat {len(duplicate)}, buah duplicate yaitu {tuple(duplicate)}")
#     else:
#         print("Tidak ada duplicate")

# program_array()


array1 = set(map(int, input("Input array ke-1: ").split()))
array2 = set(map(int, input("Input array ke-1: ").split()))

duplikat = array1.intersection(array2)

if len(duplikat) > 1:
    print(f"Terdapat {len(duplikat)} buah duplikat yaitu {tuple(duplikat)}")
elif len(duplikat) == 1:
    print(f"Terdapat 1 buah duplikat yaitu ({(tuple(duplikat))})")
else:
    print("Tidak ada duplikasi ditemukan.")