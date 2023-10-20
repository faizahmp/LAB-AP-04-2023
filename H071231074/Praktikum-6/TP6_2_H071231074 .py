def cari_duplikat(array1, array2):
    set1 = set(array1)
    set2 = set(array2)
    irisan2himpunan = set1.intersection(set2)
    if irisan2himpunan:
        tuple1 = tuple(irisan2himpunan)
        print(f"Terdapat {len(list(irisan2himpunan))} buah duplikat yaitu {tuple1}")
    else:
        print("Tidak ada duplikasi ditemukan")
        
# Input
array1 = [int(x) for x in input("Input array ke-1: ").split()]
array2 = [int(x) for x in input("Input array ke-2: ").split()]

# Panggil Fungsi
cari_duplikat(array1, array2)
