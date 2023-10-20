def strings(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    max_len = max(len_s1, len_s2)

    result = ""

    for i in range(max_len):
        if i < len_s1:
            result += s1[i]
            
        if i < len_s2:
            s2=s2[::-1]
            result += s2[i]

    return result

s1=input("masukan karakter= ")
s2=input("masukan karakter= ")
s3=strings(s1,s2)
print(s3)