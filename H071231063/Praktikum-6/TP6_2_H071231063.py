array1 = input("Input array ke-1: ").split()
array1 = [int(x) for x in array1]
array2 = input("Input array ke-2: ").split()
array2 = [int(x) for x in array2]
duplikat = []
for elemen in array1:
    if elemen in array2 and elemen not in duplikat:
        duplikat.append(elemen)
if len(duplikat) == 0:
    print("Tidak ada duplikasi yang ditemukan.")
else:
    print("Terdapat", len(duplikat), "buah duplikat yaitu", tuple(duplikat))