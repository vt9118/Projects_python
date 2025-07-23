lst = list(map(int, input("Enter 5 numbers separatly by space:").split()))
print(lst)
for i in range(5):
    if lst[i] % 2 == 0:
        print(lst[i], "is even")
    elif lst[i] % 2 != 0:
        print(lst[i], "is odd")
    else:
        print(lst[i], "is zero")