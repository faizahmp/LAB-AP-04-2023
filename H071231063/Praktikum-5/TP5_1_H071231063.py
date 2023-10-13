def combine_strings(s1, s2):
    s3 = ""
    i, j = 0, -1  
    while i < len(s1) and j >= -len(s2):
        s3 += s1[i] + s2[j]
        i += 1
        j -= 1
    while i < len(s1):
        s3 += s1[i]
        i += 1
    while j >= -len(s2):
        s3 += s2[j]
        j -= 1
    return s3
s1 = input("s1= ")
s2 = input("s2= ")
s3 = combine_strings(s1, s2)
print("Hasil mixed= ",s3)