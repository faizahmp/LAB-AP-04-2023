array1 = map(int, input("Input array ke-1: ").split(" "))
array2 = map(int, input("Input array ke-2: ").split(" "))

duplikat = tuple(set(array1) & set(array2))
banyak = len(duplikat)

if len(duplikat) > 0:
    print(f"Terdapat {banyak} buah duplikat yaitu {duplikat}")
else:
    print("Tidak ada duplikat.")