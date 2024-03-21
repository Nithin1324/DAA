f1 = 0
f2 = 1
f3 = 1
n = int(input("Enter value for N:"))
for loop in range(1,n+1):
  print(f1, end=" ")
  f1 = f2
  f2 = f3
  f3 = f1 + f2
