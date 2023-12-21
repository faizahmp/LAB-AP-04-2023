# Input jumlah suku Fibonacci yang ingin dijumlahkan
print("Berapa banyak suku Fibonacci yang ingin dijumlahkan: ")
n = int(input())

# Inisialisasi variabel awal
a, b = 0, 1
suku = 0

# Menampilkan suku Fibonacci sesuai dengan input
while suku < n:
    print(a, end=" ")
    fibonacci = a + b
    a = b
    b = fibonacci
    suku += 1

# Jika input n kurang dari atau sama dengan 0
if n <= 0:
    print("Tidak ada suku Fibonacci yang akan dijumlahkan.")
