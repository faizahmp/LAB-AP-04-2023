print(f"{'PROGRAM MENENTUKAN BILANGAN':^40}")
print(f"{'FIBONACCI':^40}")
print(f"{'_'*40:^40}")
n=int(input())

a, b = 1, 0
for i in range(n):
    a, b =b, a+b
    print(a, end=' ')


