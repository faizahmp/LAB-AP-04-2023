def string_baru(inputan_str):
    if len(inputan_str)<3:
        return ("string harus lebih dari 3 kata")
    
    panjang_str= len(inputan_str)
    kata_awal=inputan_str[0]
    kata_tengah=inputan_str[panjang_str//2]
    kata_akhir= inputan_str[-1]

    string_baru=kata_awal+kata_tengah+kata_akhir
    return string_baru

input_str=input("masukan kata= ")
n=string_baru(input_str)
print(n)
        